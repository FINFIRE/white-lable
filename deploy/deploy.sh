#!/usr/bin/env bash
# Pull, build, restart. Run from /srv/finfire as the ubuntu user (member of
# the docker group). Idempotent — safe to re-run.

set -euo pipefail

REPO_DIR="/srv/finfire"
SPA_DIST="/var/www/finfire/dist"
BRANCH="${BRANCH:-tennant_mix}"

cd "$REPO_DIR"

echo "==> git fetch + checkout $BRANCH"
git fetch --all --prune
git checkout "$BRANCH"
git pull --ff-only origin "$BRANCH"

echo "==> Build the SPA"
pushd finfire_frontend >/dev/null
# npm ci is faster + reproducible when package-lock.json is in sync. Falls
# back to npm install on first run if node_modules is missing some peer.
if [[ -f package-lock.json ]]; then
    npm ci --no-audit --no-fund
else
    npm install --no-audit --no-fund
fi
npm run build
popd >/dev/null

echo "==> Sync dist/ to $SPA_DIST"
rsync -a --delete finfire_frontend/dist/ "$SPA_DIST/"

echo "==> Rebuild + restart backend container"
docker compose -f docker-compose.prod.yml build
docker compose -f docker-compose.prod.yml up -d

echo "==> Wait for gunicorn to come up"
for i in {1..30}; do
    if curl -fsS http://127.0.0.1:8000/api/health-check/ >/dev/null 2>&1; then
        echo "    backend OK"
        break
    fi
    sleep 1
    if [[ $i -eq 30 ]]; then
        echo "Backend never answered /api/health-check/ — check logs:" >&2
        echo "  docker logs finfire-api --tail=200" >&2
        exit 1
    fi
done

echo "==> Reload nginx"
sudo nginx -t
sudo systemctl reload nginx

echo "==> Done."
