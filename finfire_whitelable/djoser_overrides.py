from djoser.email import ActivationEmail, PasswordResetEmail
from djoser.serializers import (
    UserSerializer as DjoserUserSerializer,
    UserCreateSerializer as DjoserUserCreateSerializer,
    UserCreatePasswordRetypeSerializer as DjoserUserCreatePasswordRetypeSerializer,
)
from rest_framework import serializers
from django.contrib.auth.models import User


class CustomUserSerializer(DjoserUserSerializer):
    """Extends Djoser's default user serializer to include is_staff."""
    class Meta(DjoserUserSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'is_staff')


def _email_unique_in_tenant(value):
    """Reject a registration email if it already exists in the current
    tenant's auth_user table (case-insensitive). Backed by the partial
    UNIQUE index `auth_user_email_unique_ci` added in registration
    migration 0002, this serializer-level check just turns the IntegrityError
    we'd otherwise get on INSERT into a clean 400 with a field error.
    """
    if value and User.objects.filter(email__iexact=value).exists():
        raise serializers.ValidationError(
            'A user with this email already exists in this tenant.'
        )
    return value


class CustomUserCreateSerializer(DjoserUserCreateSerializer):
    """Used when DJOSER['USER_CREATE_PASSWORD_RETYPE'] is False."""
    def validate_email(self, value):
        return _email_unique_in_tenant(value)


class CustomUserCreatePasswordRetypeSerializer(DjoserUserCreatePasswordRetypeSerializer):
    """Used when DJOSER['USER_CREATE_PASSWORD_RETYPE'] is True."""
    def validate_email(self, value):
        return _email_unique_in_tenant(value)


def _tenant_aware_context(self, context):
    """Augment a djoser email context so links point at the tenant subdomain
    the request came in on, rather than any hardcoded production domain.

    djoser already derives `domain` from `RequestSite(request).domain` (i.e.
    `request.get_host()`) when neither `settings.DOMAIN` nor the sites
    framework is configured, but we set it explicitly here so the behaviour
    is obvious and resilient to djoser version churn.
    """
    request = getattr(self, "request", None)
    if request is not None:
        context["domain"] = request.get_host()
        context["protocol"] = "https" if request.is_secure() else "http"

    # Always add 'email' to context, fallback to empty string if not available
    user = self.context.get("user")
    context["email"] = (
        getattr(user, "email", "") if user else self.context.get("email", "")
    )
    return context


class CustomActivationEmail(ActivationEmail):
    def get_context_data(self):
        return _tenant_aware_context(self, super().get_context_data())


class CustomPasswordResetEmail(PasswordResetEmail):
    def get_context_data(self):
        return _tenant_aware_context(self, super().get_context_data())
