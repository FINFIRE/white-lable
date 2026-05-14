from django.db import models

from django_tenants.models import TenantMixin, DomainMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until =  models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    # White-label branding (consumed by frontend on bootstrap)
    display_name = models.CharField(max_length=120, blank=True, default='')
    logo = models.ImageField(upload_to='tenant_branding/', blank=True, null=True)
    favicon = models.ImageField(upload_to='tenant_branding/', blank=True, null=True)
    primary_color = models.CharField(max_length=9, blank=True, default='', help_text='Hex color, e.g. #1f6feb')
    accent_color = models.CharField(max_length=9, blank=True, default='')
    support_email = models.EmailField(blank=True, default='')
    contact_phone = models.CharField(max_length=40, blank=True, default='')
    signature_image = models.ImageField(upload_to='tenant_branding/', blank=True, null=True)
    signatory_name = models.CharField(max_length=120, blank=True, default='')
    signatory_title = models.CharField(
        max_length=120, blank=True, default='',
        help_text='Job title shown under the signatory name on generated letters (e.g. "Chief Revenue Officer").',
    )
    address = models.TextField(
        blank=True, default='',
        help_text='Multi-line postal address used in the letter footer.',
    )

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

    # deleting the tenant on db or sub-domain db schema is also deleted on True
    auto_drop_schema = True


    def get_domain_name(self):
        domain = self.domains.first()
        if domain:
            return domain.domain
        return None


class Domain(DomainMixin):
    pass


