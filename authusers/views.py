from django.contrib.auth import get_user_model

from rest_framework import generics, response, status
from rest_framework.permissions import IsAuthenticated


from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.views import TokenRefreshView



from .models import OtpGeneration
from .serializers import (
    ChangePasswordSerializer, 
    LoginSerializers, LogoutSerializer,

    OTPRequestSerializer, OTPVerificationSerializer,
    NewPasswordSerializers,

)


User = get_user_model()

class ChangePasswordApiView(generics.UpdateAPIView):
    http_method_names = ['patch']
    permission_classes = [IsAuthenticated,]
    serializer_class = ChangePasswordSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user


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


class TokenRefreshApiView(TokenRefreshView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # response.data.update({'access_token': response.data.pop('access')})
        # response.data.update({'refresh_token': response.data.pop('refresh')})
        # response.set_cookie(key="access_token", value=response.data.get('access_token'), httponly=True)
        # response.set_cookie(key="refresh_token", value=response.data.get('refresh_token'), httponly=True)
        return response


class OTPRequestAPIView(generics.CreateAPIView):
    http_method_names = ['post']
    permission_classes = []
    serializer_class = OTPRequestSerializer
    queryset = OtpGeneration.objects.all()


class OTPVerificationAPIView(generics.GenericAPIView):
    http_method_names = ['post']
    serializer_class = OTPVerificationSerializer
    permission_classes = []
    queryset = OtpGeneration.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, many=False)
        old_contact = request.data.get('contact')
        serializer.is_valid(raise_exception=True)
        serializer.validated_data.pop('contact')
        serializer.validated_data.update({'contact': old_contact})
        return response.Response(data=serializer.validated_data, status= status.HTTP_200_OK)


class NewPasswordApiView(generics.GenericAPIView):
    serializer_class = NewPasswordSerializers
    permission_classes = []
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return response.Response({'success':True, 'message':'Password Reset completed'}, status= status.HTTP_200_OK)
        else:
            return response.Response({'error': 'OTP is not valid or has expired, Please create a new OTP'}, status= status.HTTP_401_UNAUTHORIZED)




