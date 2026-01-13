from django.urls import path, include
from .views import vquestion1_form


#Views for the urls
urlpatterns = [
    path('vquestion1/',vquestion1_form,name='vquestion1'),
]