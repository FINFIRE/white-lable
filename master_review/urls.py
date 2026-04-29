from django.contrib import admin
from django.urls import path
from .views import superuser_dashboard,download_file,manual_match
from django.contrib.auth.models import User




urlpatterns = [
    path('master-review/', superuser_dashboard, name='master-review'),
    path('download/', download_file, name='download_file'),
    path('manual-match/', manual_match, name='manual_match'),
    ]