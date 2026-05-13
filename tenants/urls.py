from django.urls import path

from .views import (
    ListCreateClientAPIView,
    RUDClientAPIView,

    LoginApiView,
    LogoutApiView,

    TenantSuperuserCreateView,
)

urlpatterns = [

    path('', ListCreateClientAPIView.as_view()),
    path('<int:pk>/', RUDClientAPIView.as_view()),
    path('<int:pk>/create-superuser/', TenantSuperuserCreateView.as_view(), name='tenant-create-superuser'),


    path('login/', LoginApiView.as_view()),
    path('logout/', LogoutApiView.as_view()),


]



