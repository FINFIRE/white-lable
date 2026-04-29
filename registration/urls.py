from django.contrib import admin 
from django.urls import path
from .views import registration_form_view,registration_form_view2,register,login_view,home,user_logout,activate
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),
    path('registration1', registration_form_view, name='registration_form_view'),
    path('registration2', registration_form_view2, name='registration_form_view2'),
    path('registration',register,name='registration'),
    #path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('login-view',login_view,name='login_view'),
    path('logout',user_logout,name='logout_view'),
]
