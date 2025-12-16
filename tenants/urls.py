from django.urls import path

from .views import (
    ListCreateClientAPIView,
    RUDClientAPIView,

    LoginApiView,
    LogoutApiView,


)

urlpatterns = [

    path('', ListCreateClientAPIView.as_view()),
    path('<int:pk>/', RUDClientAPIView.as_view()),


    path('login/', LoginApiView.as_view()),
    path('logout/', LogoutApiView.as_view()),


]



