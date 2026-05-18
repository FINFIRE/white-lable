from rest_framework import generics, filters, response, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.pagination import LimitOffsetPagination
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.views import TokenRefreshView

from django_filters.rest_framework.backends import DjangoFilterBackend
from django_tenants.utils import schema_context, get_public_schema_name

from django.db import connection
from django.contrib.auth import get_user_model

from .models import Client
from .serializers import (
    ClientSerializer,
    LoginSerializers, LogoutSerializer,
    TenantBrandingSerializer,
    TenantSuperuserCreateSerializer,
)


User = get_user_model()


class ListCreateClientAPIView(generics.ListCreateAPIView):
    """List + create tenants. Restricted to platform admins.

    The previous behaviour allowed any caller to POST a new tenant (the
    quickest path to bootstrap a multi-tenant install). Now that the
    public funnel goes through Stripe Checkout + the token-gated
    `subscriptions.TenantOnboardingView`, the bare endpoint is locked
    down so a stranger can't mint themselves a tenant without paying.
    """
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['schema_name']
    search_fields = ['schema_name', 'domains__domain',]
    ordering_fields = ['created_on',]


class RUDClientAPIView(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'patch', 'delete']
    permission_classes = [IsAuthenticated,]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class LoginApiView(TokenRefreshView):
    serializer_class = LoginSerializers


class LogoutApiView(generics.GenericAPIView):
    http_method_names = ['post']
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer

    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh')

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return response.Response({"success": "Successfully Logout"}, status=status.HTTP_200_OK)
        except TokenError:
            return response.Response({"error": "Token is Invalid or Expire."}, status=status.HTTP_401_UNAUTHORIZED)


class TenantSuperuserCreateView(generics.GenericAPIView):
    """POST /tenants/<pk>/create-superuser/ — mint a superuser inside the
    target tenant's schema. Public-schema-only: callable only by an
    authenticated platform admin (e.g. romin), and only when the request
    hits the public URL conf (i.e. on the bare host, not a tenant subdomain).
    """
    http_method_names = ['post']
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = TenantSuperuserCreateSerializer
    queryset = Client.objects.all()

    def _is_public_request(self):
        tenant = getattr(connection, 'tenant', None)
        if tenant is None:
            return True
        return getattr(tenant, 'schema_name', 'public') == get_public_schema_name()

    def post(self, request, pk, *args, **kwargs):
        if not self._is_public_request():
            return response.Response(
                {'detail': 'Endpoint is only available on the public schema host.'},
                status=status.HTTP_403_FORBIDDEN,
            )

        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return response.Response(
                {'detail': 'Tenant not found.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        if client.schema_name == get_public_schema_name():
            return response.Response(
                {'detail': 'Cannot mint a tenant superuser inside the public schema.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        email = serializer.validated_data.get('email') or ''
        password = serializer.validated_data['password']

        with schema_context(client.schema_name):
            if User.objects.filter(username=username).exists():
                return response.Response(
                    {'username': ['A user with that username already exists in this tenant.']},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user = User.objects.create_superuser(
                username=username, email=email, password=password,
            )
            return response.Response(
                {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'tenant_schema': client.schema_name,
                    'tenant_id': client.id,
                },
                status=status.HTTP_201_CREATED,
            )


class TenantBrandingView(generics.GenericAPIView):
    """GET /api/branding/ — returns branding for the current tenant resolved
    from the request host. Public so the frontend can theme before login.
    """
    http_method_names = ['get']
    permission_classes = [AllowAny]
    serializer_class = TenantBrandingSerializer

    def get(self, request, *args, **kwargs):
        tenant = getattr(connection, 'tenant', None)
        if tenant is None or getattr(tenant, 'schema_name', 'public') == 'public':
            return response.Response(
                {'detail': 'No tenant resolved for this host.'},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.get_serializer(tenant, context={'request': request})
        return response.Response(serializer.data, status=status.HTTP_200_OK)
