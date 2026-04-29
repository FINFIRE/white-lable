from djoser.email import ActivationEmail, PasswordResetEmail
from djoser.serializers import UserSerializer as DjoserUserSerializer
from django.contrib.auth.models import User


class CustomUserSerializer(DjoserUserSerializer):
    """Extends Djoser's default user serializer to include is_staff."""
    class Meta(DjoserUserSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'is_staff')

class CustomActivationEmail(ActivationEmail):
    def get_context_data(self):
        context = super().get_context_data()
        # Always add 'email' to context, fallback to empty string if not available
        user = self.context.get("user")
        context["email"] = getattr(user, "email", "") if user else self.context.get("email", "")
        return context

class CustomPasswordResetEmail(PasswordResetEmail):
    def get_context_data(self):
        context = super().get_context_data()
        # Always add 'email' to context, fallback to empty string if not available
        user = self.context.get("user")
        context["email"] = getattr(user, "email", "") if user else self.context.get("email", "")
        return context 