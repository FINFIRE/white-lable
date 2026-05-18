"""Idempotently create the platform's Stripe Products + Prices and
persist the resulting IDs onto the local Plan rows.

Reads `STRIPE_SECRET_KEY` from settings. Runs against test or live
mode depending on which key is configured. Safe to re-run: if a Plan
row already has a `stripe_price_id`, we reuse it; otherwise we look
for an existing matching Price in Stripe before creating a new one.

Usage:
    docker compose exec -T backend python manage.py setup_stripe_plans
"""
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

import stripe

from subscriptions.models import Plan


# Catalogue of plans we offer. Keep `slug` stable — the frontend, the
# Checkout view, and the webhook all key off it.
PLAN_CATALOGUE = [
    {
        'slug': 'monthly',
        'name': 'Monthly',
        'description': 'Pay $40 per month. Cancel anytime.',
        'amount_cents': 4000,
        'currency': 'usd',
        'interval': 'month',
        'supports_trial': True,   # the "7-day free trial" button uses this plan
        'sort_order': 10,
    },
    {
        'slug': 'yearly',
        'name': 'Yearly',
        'description': 'Pay $360 per year (saves $120 vs. monthly).',
        'amount_cents': 36000,
        'currency': 'usd',
        'interval': 'year',
        'supports_trial': False,
        'sort_order': 20,
    },
]

PRODUCT_NAME_PREFIX = 'FINFIRE - '


class Command(BaseCommand):
    help = ('Create/reconcile Stripe Products and recurring Prices for the '
            'subscription plans, and persist the IDs onto Plan rows.')

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would change without calling Stripe.',
        )

    def handle(self, *args, **opts):
        if not settings.STRIPE_SECRET_KEY:
            raise CommandError(
                'STRIPE_SECRET_KEY is not set. Configure it in .env first.'
            )
        stripe.api_key = settings.STRIPE_SECRET_KEY
        dry = opts['dry_run']

        for plan_def in PLAN_CATALOGUE:
            self.stdout.write(self.style.NOTICE(f'\n--- plan: {plan_def["slug"]} ---'))
            plan, created = Plan.objects.get_or_create(
                slug=plan_def['slug'],
                defaults={
                    'name': plan_def['name'],
                    'description': plan_def['description'],
                    'amount_cents': plan_def['amount_cents'],
                    'currency': plan_def['currency'],
                    'interval': plan_def['interval'],
                    'supports_trial': plan_def['supports_trial'],
                    'sort_order': plan_def['sort_order'],
                },
            )
            if not created:
                # Keep local copy in sync with the catalogue (description,
                # supports_trial, sort_order may evolve over time).
                plan.name = plan_def['name']
                plan.description = plan_def['description']
                plan.amount_cents = plan_def['amount_cents']
                plan.currency = plan_def['currency']
                plan.interval = plan_def['interval']
                plan.supports_trial = plan_def['supports_trial']
                plan.sort_order = plan_def['sort_order']
            self.stdout.write(f'  local Plan row: {"created" if created else "updated"}  pk={plan.pk}')

            product_id = plan.stripe_product_id or self._find_or_create_product(plan, dry=dry)
            price_id = plan.stripe_price_id or self._find_or_create_price(plan, product_id, dry=dry)

            if dry:
                self.stdout.write('  (dry-run: not persisting Stripe IDs)')
                continue

            with transaction.atomic():
                plan.stripe_product_id = product_id
                plan.stripe_price_id = price_id
                plan.save()
            self.stdout.write(self.style.SUCCESS(
                f'  Stripe Product: {product_id}\n  Stripe Price:   {price_id}'
            ))

        self.stdout.write(self.style.SUCCESS('\nAll plans reconciled.'))

    # ── Stripe lookup helpers ──────────────────────────────────────────

    def _product_name(self, plan):
        return f'{PRODUCT_NAME_PREFIX}{plan.name}'

    def _find_or_create_product(self, plan, *, dry):
        """Find an existing Stripe Product by name, or create one."""
        name = self._product_name(plan)
        # Stripe doesn't index by name — list and filter. Modest catalogue
        # so iterating is fine.
        for prod in stripe.Product.list(active=True, limit=100).auto_paging_iter():
            if prod.name == name:
                self.stdout.write(f'  found existing Stripe Product "{name}" -> {prod.id}')
                return prod.id

        if dry:
            self.stdout.write(self.style.WARNING(f'  would create Stripe Product "{name}"'))
            return '<dry-run-product>'

        prod = stripe.Product.create(
            name=name,
            description=plan.description or None,
            metadata={'plan_slug': plan.slug},
        )
        self.stdout.write(f'  created Stripe Product "{name}" -> {prod.id}')
        return prod.id

    def _find_or_create_price(self, plan, product_id, *, dry):
        """Find a recurring Price on the product matching our amount+interval,
        or create one. Stripe Prices are immutable — to change the amount,
        archive the old one and create a new Price."""
        for price in stripe.Price.list(
            product=product_id, active=True, limit=100,
        ).auto_paging_iter():
            recurring = getattr(price, 'recurring', None) or {}
            if (
                price.unit_amount == plan.amount_cents
                and price.currency == plan.currency.lower()
                and recurring.get('interval') == plan.interval
            ):
                self.stdout.write(f'  found existing Stripe Price for {plan.slug} -> {price.id}')
                return price.id

        if dry:
            self.stdout.write(self.style.WARNING(
                f'  would create Stripe Price ${plan.amount_dollars:.2f}/{plan.interval}'
            ))
            return '<dry-run-price>'

        price = stripe.Price.create(
            product=product_id,
            unit_amount=plan.amount_cents,
            currency=plan.currency,
            recurring={'interval': plan.interval},
            metadata={'plan_slug': plan.slug},
        )
        self.stdout.write(f'  created Stripe Price -> {price.id}')
        return price.id
