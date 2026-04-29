#!/usr/bin/bash

# django-tenants requires schema-aware migrations
python3 manage.py migrate_schemas --shared
python3 manage.py migrate_schemas --tenant
python3 manage.py collectstatic --no-input

exec "$@"


