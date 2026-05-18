from django.contrib import admin

from tenants.admin import PublicTenantOnlyMixin

from .models import PendingOnboarding, Plan


# Plans are a platform-wide catalogue (single source of truth for what
# tenants can buy). They live in `public` and tenant admins should not
# see or edit them — same pattern as `Algorithm`, `Client`, `Domain`.
@admin.register(Plan)
class PlanAdmin(PublicTenantOnlyMixin, admin.ModelAdmin):
    list_display = (
        'slug', 'name', 'amount_dollars', 'interval',
        'supports_trial', 'is_active', 'stripe_price_id',
    )
    list_filter = ('interval', 'is_active', 'supports_trial')
    search_fields = ('slug', 'name', 'stripe_price_id')
    readonly_fields = ('stripe_product_id', 'stripe_price_id',
                       'created_at', 'updated_at')

    def amount_dollars(self, obj):
        return f'${obj.amount_dollars:.2f}'
    amount_dollars.short_description = 'Price'


@admin.register(PendingOnboarding)
class PendingOnboardingAdmin(PublicTenantOnlyMixin, admin.ModelAdmin):
    """Per-onboarding records: payment received, tenant not yet created.
    Useful for debugging stuck or abandoned signups. Read-only — these
    are managed by the webhook and the onboarding endpoint."""
    list_display = (
        'email', 'company_name', 'plan', 'with_trial',
        'status', 'created_at', 'onboarded_client',
    )
    list_filter = ('status', 'with_trial', 'plan')
    search_fields = ('email', 'company_name', 'stripe_session_id',
                     'stripe_customer_id', 'stripe_subscription_id')
    readonly_fields = (
        'stripe_session_id', 'stripe_customer_id', 'stripe_subscription_id',
        'plan', 'with_trial', 'email', 'company_name', 'onboarding_token',
        'status', 'onboarded_client',
        'created_at', 'paid_at', 'completed_at',
    )

    def has_add_permission(self, request, *args, **kwargs):
        return False  # only the webhook creates these
