"""Subscription catalogue.

`Plan` rows describe what tenants can buy: a billing cadence
(month/year) and the Stripe Price that backs it. They are
platform-wide (one set of plans, all tenants pick from them) and
therefore live in the public schema — the `subscriptions` app is in
SHARED_APPS only.

We do not store *Subscription state* here yet — that lives directly
on `tenants.Client` for the v1 implementation (one current subscription
per tenant, denormalised so we can gate access with a single query).
A separate Subscription model can grow out of this later if/when we
need history, dunning, or per-tenant multiple subscriptions.
"""
import uuid

from django.conf import settings
from django.db import models


class Plan(models.Model):
    """A purchasable billing tier backed by a Stripe Price."""

    INTERVAL_MONTH = 'month'
    INTERVAL_YEAR = 'year'
    INTERVAL_CHOICES = [
        (INTERVAL_MONTH, 'Monthly'),
        (INTERVAL_YEAR, 'Yearly'),
    ]

    slug = models.SlugField(
        max_length=64, unique=True,
        help_text='Stable identifier referenced by the frontend (e.g. "monthly").',
    )
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, default='')

    # Stripe identifiers — populated by the `setup_stripe_plans`
    # management command. We never hardcode price IDs in source.
    stripe_product_id = models.CharField(max_length=120, blank=True, default='')
    stripe_price_id = models.CharField(max_length=120, blank=True, default='')

    amount_cents = models.PositiveIntegerField(
        help_text='Price in the smallest currency unit (e.g. cents for USD).',
    )
    currency = models.CharField(max_length=3, default='usd')
    interval = models.CharField(max_length=10, choices=INTERVAL_CHOICES)
    supports_trial = models.BooleanField(
        default=False,
        help_text='If True, Checkout sessions for this plan can request a '
                  'trial via `subscription_data.trial_period_days`.',
    )
    is_active = models.BooleanField(
        default=True,
        help_text='Whether this plan is currently offered on the pricing page.',
    )

    sort_order = models.PositiveSmallIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort_order', 'amount_cents']
        verbose_name = 'Subscription plan'
        verbose_name_plural = 'Subscription plans'

    def __str__(self):
        return f'{self.name} (${self.amount_cents / 100:.2f}/{self.interval})'

    @property
    def amount_dollars(self):
        return self.amount_cents / 100


class PendingOnboarding(models.Model):
    """Bridge between a successful Stripe Checkout payment and a tenant
    creation. The webhook handler creates one of these when
    `checkout.session.completed` fires; the success page polls for the
    `onboarding_token`; the `/api/tenants/onboard/` endpoint consumes
    that token (single-use) to create the actual tenant.

    Lives in the public schema (subscriptions is in SHARED_APPS only)
    because tenants don't exist yet at this point in the flow.
    """

    STATUS_PENDING = 'pending'        # paid in Stripe, awaiting onboarding form
    STATUS_ONBOARDED = 'onboarded'    # tenant created, token consumed
    STATUS_EXPIRED = 'expired'        # too old / abandoned
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_ONBOARDED, 'Onboarded'),
        (STATUS_EXPIRED, 'Expired'),
    ]

    # Stripe identifiers — only one of these is set initially; the
    # subscription_id arrives later via the customer.subscription.created
    # event but we capture what we have on checkout.session.completed.
    stripe_session_id = models.CharField(max_length=255, unique=True)
    stripe_customer_id = models.CharField(max_length=255, blank=True, default='')
    stripe_subscription_id = models.CharField(max_length=255, blank=True, default='')

    # What the visitor bought + how to reach them.
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, related_name='pending_onboardings')
    with_trial = models.BooleanField(default=False)
    email = models.EmailField()
    company_name = models.CharField(max_length=200, blank=True, default='')

    # Single-use opaque token handed to the success page after Stripe
    # confirms payment. Sent back to /api/tenants/onboard/ to identify
    # the prepaid slot we should attach the new Client to.
    onboarding_token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING,
    )
    onboarded_client = models.ForeignKey(
        'tenants.Client', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='+',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Pending onboarding'
        verbose_name_plural = 'Pending onboardings'
        indexes = [
            models.Index(fields=['status', 'created_at']),
            models.Index(fields=['stripe_customer_id']),
        ]
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.email} ({self.plan.slug}, {self.status})'
