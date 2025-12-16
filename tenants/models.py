from django.db import models

from django_tenants.models import TenantMixin, DomainMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until =  models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

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


