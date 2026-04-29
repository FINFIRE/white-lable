from django.urls import path
from .views import iquestion1_form, iquestion2_form 

urlpatterns = [
    path('iquestion1/',iquestion1_form,name='iquestion1'),
    path('iquestion2/',iquestion2_form,name='iquestion2'),
]
