"""Operational notification emails for the subscription funnel.

These go to the platform team (settings.PLATFORM_NOTIFICATION_EMAILS),
not to the tenant's own support address. Failure is swallowed so an
SMTP outage can't block a paying customer from completing onboarding.
"""
from __future__ import annotations

import logging

from django.conf import settings
from django.core.mail import send_mail


logger = logging.getLogger(__name__)


# Body shown beneath the tenant + Stripe details. Kept as a module-level
# constant so it's easy to update when the test phase ends without
# touching the dispatch code.
TEST_PHASE_NOTICE = (
    "TEST PHASE NOTICE\n"
    "  - The Stripe amount paid is arbitrary.\n"
    "  - The funds are NOT real in the Stripe account.\n"
    "  - The Stripe integration is currently using test keys; it is\n"
    "    not linked to FINFIRE's production Stripe account yet.\n"
    "  - Once the test phase looks good to you, please provide API or\n"
    "    admin access so we can integrate FINFIRE's real Stripe\n"
    "    account."
)


def _format_tenant_paid_body(client, pending_onboarding, domain) -> str:
    po = pending_onboarding
    trial_note = (
        f"yes ({settings.STRIPE_TRIAL_DAYS}-day free trial)"
        if po.with_trial else 'no'
    )
    plan_amount = (
        f"${po.plan.amount_dollars:.2f} / {po.plan.interval}"
        if po.plan_id else 'n/a'
    )
    return (
        "Hello FINFIRE team,\n\n"
        "A new tenant just signed up and paid via Stripe:\n\n"
        f"  Company:                {client.name}\n"
        f"  Display name:           {client.display_name or '(blank)'}\n"
        f"  Subdomain / domain:     {domain or client.schema_name}\n"
        f"  Admin email:            {po.email}\n"
        f"  Plan:                   {po.plan.slug}  ({plan_amount})\n"
        f"  Trial active:           {trial_note}\n"
        f"  Subscription status:    {client.subscription_status or '(unknown)'}\n"
        f"  Stripe customer ID:     {client.stripe_customer_id or '(none)'}\n"
        f"  Stripe subscription ID: {client.stripe_subscription_id or '(none)'}\n\n"
        f"{TEST_PHASE_NOTICE}\n\n"
        "-- Automated notification from the FINFIRE platform."
    )


def notify_platform_team_of_new_tenant(client, pending_onboarding, domain=None) -> bool:
    """Send the platform team an email summarising a newly paid + onboarded
    tenant. Returns True when the send succeeded, False otherwise.

    Never raises — any error is logged so a transient SMTP problem
    can't take down the onboarding flow.
    """
    recipients = list(getattr(settings, 'PLATFORM_NOTIFICATION_EMAILS', []) or [])
    if not recipients:
        logger.info(
            'PLATFORM_NOTIFICATION_EMAILS is empty; skipping new-tenant notification for %s',
            client.schema_name,
        )
        return False

    subject = f'[FINFIRE] New tenant onboarded: {client.name}'
    body = _format_tenant_paid_body(client, pending_onboarding, domain)
    from_email = (
        getattr(settings, 'DEFAULT_FROM_EMAIL', None)
        or settings.EMAIL_HOST_USER
    )

    try:
        send_mail(
            subject=subject,
            message=body,
            from_email=from_email,
            recipient_list=recipients,
            fail_silently=False,
        )
    except Exception as exc:  # pragma: no cover - defensive
        logger.warning(
            'Failed to send platform new-tenant notification for %s: %s',
            client.schema_name, exc,
        )
        return False
    return True
