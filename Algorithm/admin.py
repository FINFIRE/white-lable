from django.contrib import admin

from tenants.admin import PublicTenantOnlyMixin

from .models import CapitalType, capitalTypes


# These two tables hold the global matching weights and capital-type
# catalogue. They live only in the public schema (Algorithm is in
# SHARED_APPS only) and are read at request-time from every tenant via
# the search_path fallback. The data is the same for all tenants and is
# managed centrally by the platform — tenant superusers should not see
# or edit it in their own subdomain admin.
@admin.register(capitalTypes)
class CapitalTypesAdmin(PublicTenantOnlyMixin, admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ['name']


@admin.register(CapitalType)
class CapitalTypeAdmin(PublicTenantOnlyMixin, admin.ModelAdmin):
    list_display = ('id', 'namec', 'counter', 'status')
    list_filter = ('status',)
    search_fields = ('namec__name',)