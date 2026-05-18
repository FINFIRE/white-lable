from django.urls import path

from .views import (
    CheckoutSessionStatusView,
    CreateCheckoutSessionView,
    PlanListView,
    StripeWebhookView,
    TenantOnboardingView,
)


# Mounted under `/api/` in finfire_whitelable/public_urls.py
urlpatterns = [
    path('plans/', PlanListView.as_view(), name='plan-list'),
    path('checkout/create-session/', CreateCheckoutSessionView.as_view(), name='checkout-create-session'),
    path('checkout/session/<str:session_id>/', CheckoutSessionStatusView.as_view(), name='checkout-session-status'),
    path('stripe/webhook/', StripeWebhookView.as_view(), name='stripe-webhook'),
    path('tenants/onboard/', TenantOnboardingView.as_view(), name='tenant-onboard'),
]
