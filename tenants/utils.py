"""Tenant helpers shared across signal handlers and views."""
from django.db import connection
from django_tenants.utils import get_public_schema_name


def _active_tenant():
    """Return the Client row for the currently active schema, or None
    when we're in the public schema / no tenant is resolved.

    `TenantMainMiddleware` sets `connection.tenant` to a Client instance
    on HTTP requests, but `schema_context(...)` (used by signals fired
    from shell commands, tests, and direct ORM work) only sets
    `connection.schema_name`. We handle both: prefer the cached Client
    on the connection, otherwise look it up by schema name.
    """
    tenant = getattr(connection, 'tenant', None)
    public = get_public_schema_name()

    # Avoid circular import: tenants.utils ←→ tenants.models
    from tenants.models import Client

    if isinstance(tenant, Client) and tenant.schema_name != public:
        return tenant

    schema_name = getattr(connection, 'schema_name', None)
    if schema_name and schema_name != public:
        try:
            return Client.objects.get(schema_name=schema_name)
        except Client.DoesNotExist:
            return None
    return None


def tenant_notification_recipients():
    """Return the list of email addresses to notify for events that
    happen inside the currently active tenant (e.g. new-user signup,
    new match generated). Pulls `Client.support_email` for the active
    tenant; supports comma-separated addresses so a tenant can fan a
    notification out to a small team.

    Returns an empty list when no tenant is resolved (we're running in
    the public schema — e.g. the platform admin creating a tenant
    superuser via /admin/, or a shell/management command) or when the
    tenant left `support_email` blank. Callers should skip sending in
    that case rather than fall back to a hardcoded FINFIRE address,
    which no longer applies in the white-label install.
    """
    tenant = _active_tenant()
    if tenant is None:
        return []

    raw = (tenant.support_email or '').strip()
    if not raw:
        return []
    return [addr.strip() for addr in raw.split(',') if addr.strip()]
