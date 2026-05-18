"""One-shot loader for the Algorithm capital-type catalogue + matrix weights.

Source file format is a partial MySQL dump (mix of MySQL DDL with
Postgres-style identifier quoting and `\\"`-escaped JSON inside
single-quoted SQL strings), so we don't feed it through psql — we parse
the two INSERT blocks in Python and replay them through the Django ORM
into the `public` schema. `Algorithm` is in SHARED_APPS only, so the
data is reachable from every tenant via search_path fallback.

Run:
    docker compose exec -T backend python /app/scripts/import_algorithm_weights.py /app/algo_tables_pg.sql
"""
import json
import os
import re
import sys

# The script lives in /app/scripts/ inside the container; make sure /app
# (the project root with finfire_whitelable/) is on sys.path before we
# ask Django to load its settings module.
_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finfire_whitelable.settings')
django.setup()

from django.db import connection  # noqa: E402
from django_tenants.utils import schema_context, get_public_schema_name  # noqa: E402

from Algorithm.models import CapitalType, capitalTypes  # noqa: E402


def _split_top_level_commas(s):
    """Split `s` on commas that aren't inside a single-quoted string,
    respecting backslash escapes. Returns the list of parts."""
    parts, cur = [], []
    in_str = esc = False
    for ch in s:
        if esc:
            cur.append(ch)
            esc = False
        elif ch == '\\':
            cur.append(ch)
            esc = True
        elif ch == "'":
            cur.append(ch)
            in_str = not in_str
        elif ch == ',' and not in_str:
            parts.append(''.join(cur))
            cur = []
        else:
            cur.append(ch)
    parts.append(''.join(cur))
    return parts


def _iter_tuples(body):
    """Yield each `(...)` row literal from a multi-row VALUES body,
    respecting strings + backslash escapes so commas/parens inside JSON
    payloads don't break the split."""
    n = len(body)
    i = 0
    while i < n:
        i = body.find('(', i)
        if i < 0:
            return
        j = i
        depth = 0
        in_str = esc = False
        while j < n:
            ch = body[j]
            if esc:
                esc = False
            elif ch == '\\':
                esc = True
            elif ch == "'":
                in_str = not in_str
            elif not in_str:
                if ch == '(':
                    depth += 1
                elif ch == ')':
                    depth -= 1
                    if depth == 0:
                        j += 1
                        break
            j += 1
        yield body[i + 1:j - 1]  # strip outer parens
        i = j


def _strip_sql_quotes(s):
    """Convert an SQL single-quoted literal into a plain Python string."""
    s = s.strip()
    if s.startswith("'") and s.endswith("'"):
        s = s[1:-1]
    # MySQL dump escapes interior double-quotes inside JSON with \" and
    # single quotes with \'. Both become their literal char in the value.
    return s.replace('\\"', '"').replace("\\'", "'").replace('\\\\', '\\')


def parse_capital_types(text):
    """Return list of (id, name) for the Algorithm_capitaltypes table."""
    m = re.search(
        r'INSERT\s+INTO\s*"?Algorithm_capitaltypes"?\s*VALUES\s*(.*?);',
        text, re.I | re.S,
    )
    if not m:
        raise RuntimeError('Algorithm_capitaltypes INSERT block not found')
    out = []
    for tup in _iter_tuples(m.group(1)):
        parts = _split_top_level_commas(tup)
        if len(parts) != 2:
            raise RuntimeError(f'Expected 2 columns in capitaltypes row, got {len(parts)}: {tup[:80]}')
        out.append((int(parts[0].strip()), _strip_sql_quotes(parts[1])))
    return out


def parse_capital_type(text):
    """Return list of (id, matrix_weights, counterlist, counter, status, namec_id)
    for the Algorithm_capitaltype (singular) table."""
    m = re.search(
        r'INSERT\s+INTO\s*"?Algorithm_capitaltype"?\s*VALUES\s*(.*?);',
        text, re.I | re.S,
    )
    if not m:
        raise RuntimeError('Algorithm_capitaltype INSERT block not found')
    out = []
    for tup in _iter_tuples(m.group(1)):
        parts = _split_top_level_commas(tup)
        if len(parts) != 6:
            raise RuntimeError(f'Expected 6 columns in capitaltype row, got {len(parts)}: {tup[:80]}')
        id_ = int(parts[0].strip())
        matrix_weights = json.loads(_strip_sql_quotes(parts[1]))
        counterlist = json.loads(_strip_sql_quotes(parts[2]))
        counter = int(parts[3].strip())
        status = bool(int(parts[4].strip()))
        namec_id = int(parts[5].strip())
        out.append((id_, matrix_weights, counterlist, counter, status, namec_id))
    return out


def _reset_serial(table_name, pk_column='id'):
    """Push the auto-increment sequence past the largest id we just inserted."""
    with connection.cursor() as cur:
        cur.execute(
            f"""
            SELECT setval(
                pg_get_serial_sequence('"{table_name}"', %s),
                COALESCE(MAX("{pk_column}"), 1),
                MAX("{pk_column}") IS NOT NULL
            )
            FROM "{table_name}";
            """,
            [pk_column],
        )


def main():
    if len(sys.argv) < 2:
        print('usage: import_algorithm_weights.py <path-to-algo_tables_pg.sql>')
        sys.exit(2)
    path = sys.argv[1]
    text = open(path, encoding='utf-8').read()

    capital_types = parse_capital_types(text)
    capital_type_rows = parse_capital_type(text)
    print(f'parsed: {len(capital_types)} capitalTypes rows, {len(capital_type_rows)} CapitalType rows')

    # Algorithm is in SHARED_APPS only, so its tables exist in public.
    # Be explicit so a wayward tenant context can't redirect us.
    with schema_context(get_public_schema_name()):
        # CapitalType has an FK to capitalTypes (on_delete=CASCADE), so we
        # have to clear the child table first.
        CapitalType.objects.all().delete()
        capitalTypes.objects.all().delete()

        capitalTypes.objects.bulk_create([
            capitalTypes(id=id_, name=name) for id_, name in capital_types
        ])
        CapitalType.objects.bulk_create([
            CapitalType(
                id=id_,
                matrix_weights=matrix_weights,
                counterlist=counterlist,
                counter=counter,
                status=status,
                namec_id=namec_id,
            )
            for (id_, matrix_weights, counterlist, counter, status, namec_id)
            in capital_type_rows
        ])

        # Reset the bigserial sequences so the next ORM-driven insert
        # picks an id beyond the largest one we just bulk-loaded.
        _reset_serial('Algorithm_capitaltypes')
        _reset_serial('Algorithm_capitaltype')

        # Sanity counts
        ct_count = capitalTypes.objects.count()
        wt_count = CapitalType.objects.count()
        print(f'loaded:  {ct_count} capitalTypes rows, {wt_count} CapitalType rows')


if __name__ == '__main__':
    main()
