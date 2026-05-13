from django import forms
from django.contrib import admin, messages
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import path, reverse
from django.utils.html import format_html

from django_tenants.utils import get_public_schema_name, schema_context

from tenants.models import Client, Domain


User = get_user_model()


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


class TenantSuperuserAdminForm(forms.Form):
    """Admin form for creating a superuser inside a tenant's schema."""
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=254, required=False)
    password = forms.CharField(
        widget=forms.PasswordInput, min_length=6, required=True,
        help_text='Minimum 6 characters.',
    )


@admin.register(Client)
class ClientAdmin(PublicTenantOnlyMixin, admin.ModelAdmin):
    """Manage tenants. Only visible/usable on the public-schema host —
    a tenant's own superuser logging in via their subdomain will not see
    this app in the admin index, nor be able to reach any of its URLs."""
    list_display = ('name', 'schema_name', 'paid_until', 'create_superuser_link')
    readonly_fields = ()

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                '<int:object_id>/create-superuser/',
                self.admin_site.admin_view(self.create_superuser_view),
                name='tenants_client_create_superuser',
            ),
        ]
        return custom + urls

    def create_superuser_link(self, obj):
        """Per-row link in the changelist to mint a tenant superuser."""
        if obj.schema_name == get_public_schema_name():
            return '—'
        url = reverse('admin:tenants_client_create_superuser', args=[obj.pk])
        return format_html(
            '<a class="button" href="{}" '
            'style="background:#2563EB;color:#fff;padding:4px 10px;border-radius:4px;'
            'text-decoration:none;font-size:12px">Create superuser</a>',
            url,
        )
    create_superuser_link.short_description = 'Tenant Superuser'

    def create_superuser_view(self, request, object_id):
        """Custom admin view that mints a superuser inside the tenant schema."""
        # Belt + braces: PublicTenantOnlyMixin already hides the section from
        # tenant-subdomain admins, but block the URL directly too in case
        # someone hand-types it on a tenant subdomain.
        if hasattr(request, 'tenant') and request.tenant.schema_name != get_public_schema_name():
            messages.error(
                request,
                'This action is only available on the public-schema admin.',
            )
            return HttpResponseRedirect(reverse('admin:index'))
        if not request.user.is_superuser:
            messages.error(request, 'Only platform superusers can create tenant superusers.')
            return HttpResponseRedirect(reverse('admin:tenants_client_changelist'))

        client = get_object_or_404(Client, pk=object_id)

        if client.schema_name == get_public_schema_name():
            messages.error(
                request,
                'Cannot mint a tenant superuser inside the public schema.',
            )
            return HttpResponseRedirect(reverse('admin:tenants_client_changelist'))

        if request.method == 'POST':
            form = TenantSuperuserAdminForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data.get('email') or ''
                password = form.cleaned_data['password']

                with schema_context(client.schema_name):
                    if User.objects.filter(username=username).exists():
                        form.add_error(
                            'username',
                            'A user with that username already exists in this tenant.',
                        )
                    else:
                        User.objects.create_superuser(
                            username=username, email=email, password=password,
                        )
                        messages.success(
                            request,
                            f'Superuser "{username}" created in tenant '
                            f'"{client.schema_name}".',
                        )
                        return HttpResponseRedirect(
                            reverse('admin:tenants_client_changelist')
                        )
        else:
            form = TenantSuperuserAdminForm()

        context = {
            **self.admin_site.each_context(request),
            'title': f'Create superuser for tenant: {client.name}',
            'client': client,
            'form': form,
            'opts': self.model._meta,
            'has_view_permission': True,
        }
        return render(
            request,
            'admin/tenants/client/create_superuser.html',
            context,
        )


@admin.register(Domain)
class DomainAdmin(PublicTenantOnlyMixin, admin.ModelAdmin):
    """Tenant <-> host mapping; public-schema only for the same reason as ClientAdmin."""
    list_display = ('domain', 'tenant', 'is_primary')
