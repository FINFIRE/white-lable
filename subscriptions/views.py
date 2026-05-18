"""Stripe Checkout + tenant onboarding endpoints.

All views in this module live on the public URL conf — they're used
*before* a tenant exists. The flow:

  1.  Marketing page  -> POST /api/checkout/create-session/
                         -> Stripe Checkout URL
  2.  Stripe Checkout (hosted)  -> payment success
  3.  Stripe webhook  -> POST /api/stripe/webhook/
                         -> PendingOnboarding(status=pending) row
  4.  Success page    -> GET /api/checkout/session/{id}/
                         -> {paid:true, onboarding_token:...} once webhook ran
  5.  Onboarding form -> POST /api/tenants/onboard/
                         -> creates Client + Domain + admin user
                         -> marks PendingOnboarding as onboarded
"""
from datetime import datetime, timezone

import stripe
from django.conf import settings
from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django_tenants.utils import schema_context
from rest_framework import generics, response, status, views
from rest_framework.permissions import AllowAny

from tenants.models import Client, Domain
from tenants.serializers import ClientSerializer

from .models import PendingOnboarding, Plan
from .serializers import (
    CreateCheckoutSessionSerializer,
    PlanPublicSerializer,
    TenantOnboardingSerializer,
)


def _frontend_base_url(request):
    """The URL Stripe should redirect the browser to after checkout.
    Pulls from settings.FRONTEND_BASE_URL if set (prod), otherwise falls
    back to the request host (dev — Vite proxies to backend with the
    `acme.localhost:5173`-style Host header preserved, so this resolves
    to the React dev server)."""
    explicit = getattr(settings, 'FRONTEND_BASE_URL', '')
    if explicit:
        return explicit.rstrip('/')
    return request.build_absolute_uri('/').rstrip('/')


# ── Pricing endpoint ───────────────────────────────────────────────────


class PlanListView(generics.ListAPIView):
    """GET /api/plans/ — returns the active plan catalogue for the
    marketing pricing page. Public."""
    permission_classes = [AllowAny]
    serializer_class = PlanPublicSerializer
    queryset = Plan.objects.filter(is_active=True)


# ── Checkout: create a Stripe session ──────────────────────────────────


class CreateCheckoutSessionView(generics.GenericAPIView):
    """POST /api/checkout/create-session/

    Body: {plan: 'monthly'|'yearly', with_trial: bool, email, company_name}
    Returns: {checkout_url, session_id}
    """
    permission_classes = [AllowAny]
    serializer_class = CreateCheckoutSessionSerializer

    def post(self, request, *args, **kwargs):
        if not settings.STRIPE_SECRET_KEY:
            return response.Response(
                {'detail': 'Billing is not configured. Contact support.'},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        plan: Plan = data['plan']
        with_trial: bool = data['with_trial']
        email: str = data['email']
        company_name: str = data.get('company_name', '')

        if not plan.stripe_price_id:
            return response.Response(
                {'detail': f'Plan "{plan.slug}" is missing a Stripe price. '
                           f'Run `manage.py setup_stripe_plans`.'},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        stripe.api_key = settings.STRIPE_SECRET_KEY
        frontend = _frontend_base_url(request)

        # The session_id placeholder is filled by Stripe before redirect.
        success_url = (
            f'{frontend}/checkout/success?session_id={{CHECKOUT_SESSION_ID}}'
        )
        cancel_url = f'{frontend}/pricing?canceled=1'

        # Metadata travels with the Checkout Session and the resulting
        # Subscription, so the webhook can recover what we need without
        # any local state pre-payment.
        metadata = {
            'plan_slug': plan.slug,
            'with_trial': 'true' if with_trial else 'false',
            'company_name': company_name,
        }
        subscription_data = {'metadata': metadata}
        if with_trial and plan.supports_trial:
            subscription_data['trial_period_days'] = settings.STRIPE_TRIAL_DAYS

        try:
            session = stripe.checkout.Session.create(
                mode='subscription',
                payment_method_types=['card'],
                line_items=[{'price': plan.stripe_price_id, 'quantity': 1}],
                customer_email=email,
                allow_promotion_codes=True,
                success_url=success_url,
                cancel_url=cancel_url,
                metadata=metadata,
                subscription_data=subscription_data,
            )
        except stripe.error.StripeError as exc:
            return response.Response(
                {'detail': f'Stripe error: {exc.user_message or str(exc)}'},
                status=status.HTTP_502_BAD_GATEWAY,
            )

        return response.Response(
            {'session_id': session.id, 'checkout_url': session.url},
            status=status.HTTP_201_CREATED,
        )


# ── Stripe webhook ─────────────────────────────────────────────────────


@method_decorator(csrf_exempt, name='dispatch')
class StripeWebhookView(views.APIView):
    """POST /api/stripe/webhook/

    Receives signed events from Stripe. Verifies the signature against
    STRIPE_WEBHOOK_SECRET (obtain via `stripe listen` in dev, or the
    Stripe Dashboard's "Add endpoint" wizard in prod).

    Reads these events:
      - checkout.session.completed: payment cleared -> create
        PendingOnboarding(status=pending) so the success page can
        hand the visitor an onboarding form.
      - customer.subscription.updated / .deleted: keep the matching
        Client.subscription_* columns in sync.
    """
    permission_classes = [AllowAny]
    authentication_classes = []  # webhook is signature-verified, no DRF auth

    def post(self, request, *args, **kwargs):
        if not settings.STRIPE_WEBHOOK_SECRET:
            return response.Response(
                {'detail': 'Webhook secret not configured.'},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        payload = request.body
        sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.STRIPE_WEBHOOK_SECRET,
            )
        except (ValueError, stripe.error.SignatureVerificationError) as exc:
            return response.Response(
                {'detail': f'Invalid webhook: {exc}'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        event_type = event['type']
        obj = event['data']['object']
        handler = getattr(self, f'_handle_{event_type.replace(".", "_")}', None)
        if handler is not None:
            handler(obj)
        # Acknowledge unknown events so Stripe doesn't retry — they're
        # subscriptions for events we may add handlers for later.
        return response.Response({'received': True}, status=status.HTTP_200_OK)

    # ---- event handlers ---------------------------------------------

    def _handle_checkout_session_completed(self, session):
        """Payment cleared. Create the PendingOnboarding row that the
        success page polls for."""
        meta = session.get('metadata') or {}
        plan_slug = meta.get('plan_slug')
        try:
            plan = Plan.objects.get(slug=plan_slug)
        except Plan.DoesNotExist:
            # Stale plan reference — log and bail (Stripe will retry,
            # but we don't want a 500 here).
            return

        defaults = {
            'plan': plan,
            'with_trial': meta.get('with_trial') == 'true',
            'email': session.get('customer_email') or session.get('customer_details', {}).get('email', ''),
            'company_name': meta.get('company_name', ''),
            'stripe_customer_id': session.get('customer') or '',
            'stripe_subscription_id': session.get('subscription') or '',
            'paid_at': datetime.now(timezone.utc),
        }
        PendingOnboarding.objects.update_or_create(
            stripe_session_id=session['id'],
            defaults=defaults,
        )

    def _handle_customer_subscription_updated(self, sub):
        self._sync_subscription_to_client(sub)

    def _handle_customer_subscription_deleted(self, sub):
        self._sync_subscription_to_client(sub)

    def _sync_subscription_to_client(self, sub):
        """Mirror the subscription state onto the matching Client row.
        The link is the stripe_subscription_id stored at onboarding time."""
        sub_id = sub.get('id')
        if not sub_id:
            return
        client = Client.objects.filter(stripe_subscription_id=sub_id).first()
        if client is None:
            return

        period_end_ts = sub.get('current_period_end')
        trial_end_ts = sub.get('trial_end')
        client.subscription_status = sub.get('status') or ''
        client.current_period_end = (
            datetime.fromtimestamp(period_end_ts, tz=timezone.utc)
            if period_end_ts else None
        )
        client.trial_end = (
            datetime.fromtimestamp(trial_end_ts, tz=timezone.utc)
            if trial_end_ts else None
        )
        client.save(update_fields=[
            'subscription_status', 'current_period_end', 'trial_end',
        ])


# ── Checkout: status poll ──────────────────────────────────────────────


class CheckoutSessionStatusView(views.APIView):
    """GET /api/checkout/session/{stripe_session_id}/

    The success page polls this until the webhook has run and a
    PendingOnboarding row exists for the session. Once it does, we
    return the onboarding_token the visitor will paste into the form.
    """
    permission_classes = [AllowAny]

    def get(self, request, session_id, *args, **kwargs):
        po = PendingOnboarding.objects.filter(stripe_session_id=session_id).first()
        if po is None:
            return response.Response(
                {'paid': False, 'reason': 'pending_webhook'},
                status=status.HTTP_200_OK,
            )

        if po.status == PendingOnboarding.STATUS_ONBOARDED:
            return response.Response(
                {'paid': True, 'already_onboarded': True},
                status=status.HTTP_200_OK,
            )

        return response.Response(
            {
                'paid': True,
                'already_onboarded': False,
                'email': po.email,
                'company_name': po.company_name,
                'plan_slug': po.plan.slug,
                'with_trial': po.with_trial,
                'onboarding_token': str(po.onboarding_token),
            },
            status=status.HTTP_200_OK,
        )


# ── Tenant onboarding (token-gated) ────────────────────────────────────


class TenantOnboardingView(generics.GenericAPIView):
    """POST /api/tenants/onboard/

    Token-gated, single-use replacement for the public POST /tenants/
    (which is now restricted to platform admins). The token is minted
    by the Stripe webhook and only valid for the matching paid-but-not-
    onboarded session. Creates the Client + Domain + admin user inside
    that tenant's schema, then marks the PendingOnboarding consumed.
    """
    permission_classes = [AllowAny]
    serializer_class = TenantOnboardingSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        # Atomically claim the pending row so two concurrent submissions
        # can't both create a tenant from the same payment.
        po = (
            PendingOnboarding.objects
            .select_for_update()
            .filter(
                onboarding_token=data['onboarding_token'],
                status=PendingOnboarding.STATUS_PENDING,
            )
            .first()
        )
        if po is None:
            return response.Response(
                {'detail': 'Invalid or already-used onboarding token.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if Client.objects.filter(schema_name=data['schema_name']).exists():
            return response.Response(
                {'schema_name': ['That subdomain is already taken.']},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Reuse the existing ClientSerializer path so the Client + Domain
        # + tenant superuser are all created with the same logic the
        # platform admin's POST /tenants/ uses.
        client_payload = {
            'schema_name': data['schema_name'],
            'name': data['company_name'],
            'paid_until': '2099-12-31',  # superseded by the live Stripe sub
            'on_trial': po.with_trial,
            'email': data['admin_email'],
            'password': data['admin_password'],
        }
        client_serializer = ClientSerializer(data=client_payload)
        client_serializer.is_valid(raise_exception=True)
        client = client_serializer.save()

        # Attach the Stripe identifiers to the freshly created Client and
        # mark the PendingOnboarding consumed.
        client.stripe_customer_id = po.stripe_customer_id
        client.stripe_subscription_id = po.stripe_subscription_id
        client.subscription_plan_slug = po.plan.slug
        client.subscription_status = 'trialing' if po.with_trial else 'active'
        client.support_email = po.email  # sensible default; admin can change
        client.save(update_fields=[
            'stripe_customer_id', 'stripe_subscription_id',
            'subscription_plan_slug', 'subscription_status', 'support_email',
        ])

        po.status = PendingOnboarding.STATUS_ONBOARDED
        po.completed_at = datetime.now(timezone.utc)
        po.onboarded_client = client
        po.save(update_fields=['status', 'completed_at', 'onboarded_client'])

        # Surface the subdomain so the success page can show a login link.
        domain = Domain.objects.filter(tenant=client).first()
        return response.Response(
            {
                'schema_name': client.schema_name,
                'name': client.name,
                'domain': domain.domain if domain else None,
                'support_email': client.support_email,
                'subscription_status': client.subscription_status,
                'subscription_plan_slug': client.subscription_plan_slug,
            },
            status=status.HTTP_201_CREATED,
        )
