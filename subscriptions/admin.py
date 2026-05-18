from django.contrib import admin

from tenants.admin import PublicTenantOnlyMixin

from .models import Plan


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
