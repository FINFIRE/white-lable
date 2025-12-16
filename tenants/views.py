from rest_framework import generics, filters, response, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.pagination import LimitOffsetPagination
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.views import TokenRefreshView

from django_filters.rest_framework.backends import DjangoFilterBackend


from .models import Client
from .serializers import (
    ClientSerializer,
    LoginSerializers, LogoutSerializer,
)


class ListCreateClientAPIView(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    permission_classes = [AllowAny,]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['schema_name']
    search_fields = ['schema_name', 'domains__domain',]
    ordering_fields = ['created_on',]

    # def get_permissions(self):
    #     if self.request.method.lower() == 'post':
    #         self.permission_classes = [AllowAny,]
    #     elif self.request.method.lower() == 'get':
    #         self.permission_classes = [IsAuthenticated, IsAdminUser,]
    #     return super().get_permissions() 


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
