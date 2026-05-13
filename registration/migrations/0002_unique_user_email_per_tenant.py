"""Per-tenant uniqueness on auth_user.email.

Stock django.contrib.auth.User.email has no DB constraint, so two users can
register with the same email inside a single tenant. We add a partial,
case-insensitive UNIQUE INDEX on auth_user.email scoped to the schema this
migration is being applied to. Because django_tenants runs each app's
migrations once per tenant schema (with the search_path scoped to that
schema), the resulting index is created independently inside every
tenant — so the constraint is naturally per-tenant: alice@example.com may
exist once in `acme` and once in `finfire`, but not twice in either.

`registration` lives in TENANT_APPS only, so this migration is never
applied to the public schema — the public auth_user keeps its existing
(non-unique) email column.

The index is partial (`WHERE email <> ''`) so users with no email recorded
do not clash with each other.
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql=(
                "CREATE UNIQUE INDEX IF NOT EXISTS auth_user_email_unique_ci "
                "ON auth_user (LOWER(email)) WHERE email <> '';"
            ),
            reverse_sql=(
                "DROP INDEX IF EXISTS auth_user_email_unique_ci;"
            ),
        ),
    ]
