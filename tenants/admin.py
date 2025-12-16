from django.contrib import admin
from django_tenants.utils import get_public_schema_name

from tenants.models import Client, Domain


class PublicTenantOnlyMixin:
    """Allow Access to Public Tenant Only."""
    def _only_public_tenant_access(self, request):
            if hasattr(request, 'tenant'):
                return True if request.tenant.schema_name == get_public_schema_name() else False
            return True
    
    def has_view_permission(self,request, view=None):
            return self._only_public_tenant_access(request)
    
    def has_add_permission(self,request, view=None):
            return self._only_public_tenant_access(request)
    
    def has_change_permission(self,request, view=None):
            return self._only_public_tenant_access(request)
    
    def has_delete_permission(self,request, view=None):
            return self._only_public_tenant_access( request)
    
    def has_view_or_change_permission(self,request, view=None):
            return self._only_public_tenant_access(request)



@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'paid_until')


admin.site.register(Domain)

