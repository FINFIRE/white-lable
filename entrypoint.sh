#!/usr/bin/bash
#
# Container entrypoint — runs once on every backend container start.
# Every step here is idempotent so a restart is safe.

# ── Schema-aware migrations (django-tenants) ───────────────────────────
python3 manage.py migrate_schemas --shared
python3 manage.py migrate_schemas --tenant
python3 manage.py collectstatic --no-input

# ── Platform-admin bootstrap ───────────────────────────────────────────
# Creates a public-schema superuser on a fresh deploy; skips if the
# username already exists, so this is safe to run on every restart.
#
# Defaults match the credentials the platform owner asked for on first
# deploy. They are intentionally weak so the first login is easy —
# rotate the password from Django admin (or by re-running this entrypoint
# with PLATFORM_ADMIN_PASSWORD set in the prod env) immediately after
# the first successful login.
export PLATFORM_ADMIN_USERNAME="${PLATFORM_ADMIN_USERNAME:-finfire}"
export PLATFORM_ADMIN_EMAIL="${PLATFORM_ADMIN_EMAIL:-tony@tonydrexelsmith.com}"
export PLATFORM_ADMIN_PASSWORD="${PLATFORM_ADMIN_PASSWORD:-development}"

python3 manage.py shell <<'PY'
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ['PLATFORM_ADMIN_USERNAME']
email    = os.environ['PLATFORM_ADMIN_EMAIL']
password = os.environ['PLATFORM_ADMIN_PASSWORD']

if User.objects.filter(username=username).exists():
    print(f"[bootstrap] Platform superuser '{username}' already exists; skipping.")
else:
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"[bootstrap] Created platform superuser '{username}' ({email}).")
PY

# ── Stripe Products + Prices ───────────────────────────────────────────
# Idempotent: existing Products/Prices are reused, missing ones created
# and their IDs persisted onto Plan rows. Failures are logged but never
# abort startup — Stripe being unreachable for a few seconds shouldn't
# take the backend down.
python3 manage.py setup_stripe_plans || \
    echo "[bootstrap] setup_stripe_plans exited non-zero — see logs above."

# ── Matching-algorithm weights into the public schema ─────────────────
# Re-imports the 100 capital types + matrix weights from the SQL dump
# committed alongside the repo. The script wipes child rows + parent
# rows before re-inserting, so re-running on each container start keeps
# the catalogue in sync with whatever is in algo_tables_pg.sql. Always
# runs *before* the server starts accepting traffic (the `exec` below),
# so there's no risk of a request seeing a partial wipe.
ALGO_SQL="${ALGO_SQL:-/app/algo_tables_pg.sql}"
if [ -f "${ALGO_SQL}" ]; then
    python3 /app/scripts/import_algorithm_weights.py "${ALGO_SQL}" || \
        echo "[bootstrap] import_algorithm_weights.py exited non-zero — see logs above."
else
    echo "[bootstrap] ${ALGO_SQL} not found; skipping algorithm-weight import."
fi

exec "$@"
