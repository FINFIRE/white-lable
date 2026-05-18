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

    # ── Subscription state ────────────────────────────────────────────
    # Denormalised from the Stripe Subscription so we can gate access
    # with one query. The canonical source of truth is Stripe (and the
    # `stripe_subscription_id` lookup); these columns are written by
    # the webhook handler.
    stripe_customer_id = models.CharField(max_length=120, blank=True, default='')
    stripe_subscription_id = models.CharField(max_length=120, blank=True, default='')
    subscription_status = models.CharField(
        max_length=32, blank=True, default='',
        help_text='Latest Stripe status: trialing / active / past_due / '
                  'canceled / incomplete / incomplete_expired / unpaid.',
    )
    subscription_plan_slug = models.CharField(
        max_length=64, blank=True, default='',
        help_text='Slug of the subscriptions.Plan currently in effect '
                  '(e.g. "monthly", "yearly").',
    )
    current_period_end = models.DateTimeField(blank=True, null=True)
    trial_end = models.DateTimeField(blank=True, null=True)

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


