from django.urls import path

from .views import (

    ChangePasswordApiView,

    LoginApiView,
    LogoutApiView,
    TokenRefreshApiView,


    # OTP views
    OTPRequestAPIView,
    OTPVerificationAPIView,
    NewPasswordApiView,
)

urlpatterns = [
    path('login/', LoginApiView.as_view(), name='login'),
    path('logout/', LogoutApiView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshApiView.as_view(), name='token-refresh'),

    path('users/change-password/', ChangePasswordApiView.as_view(), name='change-password'),

    path('otp/request/', OTPRequestAPIView.as_view(), name='otp-request'),
    path('otp/verify/', OTPVerificationAPIView.as_view(), name='otp-verify'),
    path('otp/new-password/', NewPasswordApiView.as_view(), name='new-password'),


]


