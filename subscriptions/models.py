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
