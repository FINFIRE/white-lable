from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django_tenants.utils import schema_context

from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers

from finfire_whitelable.settings import env


from .models import Client, Domain


User = get_user_model()

class ClientSerializer(serializers.ModelSerializer):

    domain = serializers.CharField(source="get_domain_name", read_only=True)

    email = serializers.EmailField(max_length=256, required=True, write_only=True)
    password = serializers.CharField(write_only=True, allow_blank=True, required=False)

    class Meta:
        model = Client
        fields = '__all__'

    def validate(self, attrs):
        schema_name = attrs.get('schema_name')

        # during creation only
        if (not self.instance) and Client.objects.filter(schema_name=schema_name).exists():
                raise serializers.ValidationError({"schema_name": "Schema name already exists."})
            
        if self.instance and 'schema_name' in attrs:
            raise serializers.ValidationError({"schema_name": "Cannot update schema after setting once."})
        
        return super().validate(attrs)

    def create(self, validated_data):
        schema_name = validated_data.get('schema_name')

        email = validated_data.pop('email')
        password = validated_data.pop('password', None)

        client = super().create(validated_data)

        Domain.objects.create(
            tenant=client,
            domain=_resolve_tenant_domain(schema_name),
        )

        # creating user in that domain so that user can login as super user
        with schema_context(client.schema_name):
            user = User.objects.create_superuser(
                username=email, email=email, password=password,
            )
            user.save()

        return client


def _resolve_tenant_domain(schema_name):
    """Build the public-facing host for a new tenant from env config.

    `HOST_ENV` controls the format:
      - 'local'                    -> "<schema>.localhost"
      - 'prod' / 'staging' / 'dev' -> "<schema>.<DOMAIN>"

    Misconfiguration is treated as a hard error rather than silently
    producing `<schema>.localhost`, because that mistake only surfaces
    when a real tenant signs up in production — too late to notice
    cleanly. Set both vars in the prod `.env` on the host:
        HOST_ENV=prod
        DOMAIN=appfinfire.com
    """
    environment = (env('HOST_ENV', default='') or '').strip().lower()
    if environment == 'local':
        return f'{schema_name}.localhost'
    if not environment:
        raise serializers.ValidationError({
            'detail': (
                'HOST_ENV is not configured on this deployment. Set '
                'HOST_ENV=prod (or "staging" / "dev") plus DOMAIN=<root-domain> '
                'in the server .env before onboarding tenants.'
            ),
        })
    domain = (env('DOMAIN', default='') or '').strip()
    if not domain:
        raise serializers.ValidationError({
            'detail': (
                f'DOMAIN is not configured (HOST_ENV={environment!r}). '
                f'Set DOMAIN=<your-root-domain> (e.g. "appfinfire.com") in .env.'
            ),
        })
    return f'{schema_name}.{domain}'


class LoginSerializers(TokenObtainPairSerializer):
    """Checks if user has verified email or not"""
    email = serializers.CharField(max_length=66, write_only=True)
    password = serializers.CharField(max_length = 68, min_length=6, write_only=True)

    access = serializers.CharField(max_length=555, read_only=True)
    refresh = serializers.CharField(max_length=555, read_only=True)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role
        return token

    def validate(self, attrs):
        email = attrs.get('email', '')
        
        user = User.objects.filter(email=email).first()
        
        user = authenticate(**attrs)
        if not user:
            raise AuthenticationFailed('Invalid Credential, Try again')
        
        refresh = self.get_token(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(max_length=256, required=True)


class TenantSuperuserCreateSerializer(serializers.Serializer):
    """Body for POST /tenants/<pk>/create-superuser/.
    Used by a public-schema admin (e.g. the platform owner) to mint a
    superuser inside an existing tenant's schema without shell access.
    """
    username = serializers.CharField(max_length=150, required=True)
    email = serializers.EmailField(max_length=254, required=False, allow_blank=True)
    password = serializers.CharField(write_only=True, required=True, min_length=6)


class TenantBrandingSerializer(serializers.ModelSerializer):
    """Public read-only branding payload for the active tenant.
    Resolved via django_tenants from the request host, so the frontend can
    fetch /api/branding/ with no auth and render tenant-specific theme.
    """
    domain = serializers.CharField(source='get_domain_name', read_only=True)

    class Meta:
        model = Client
        fields = (
            'schema_name', 'name', 'display_name', 'domain',
            'logo', 'favicon', 'primary_color', 'accent_color',
            'support_email', 'contact_phone',
            'signature_image', 'signatory_name', 'signatory_title',
            'address',
        )


