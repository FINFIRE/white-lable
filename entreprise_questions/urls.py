from django.urls import path
from .views import equestion_formb,equestion_forma,equestion1_form, equestion2_form,equestion3_form,equestion4_form,\
    equestion5_form,equestion6_form,equestion7_form,equestion8_form,equestion9_form,\
    equestion10_form,equestion11_form,equestion12_form,equestion13_form,equestion14_form,documentsprepared_form,preRating, referral_response_view,lendig_requirements_views

urlpatterns = [
    path('equestion/',equestion_forma,name='equestion'),
    path('equestionb/',equestion_formb,name='equestionb'),
    path('equestion1/',equestion1_form,name='equestion1'),
    path('equestion2/',equestion2_form,name='equestion2'),
    path('eqeustion3/',equestion3_form,name='equestion3'),
    path('equestion4/',equestion4_form,name ='equestion4'),
    path('equestion5/',equestion5_form,name='equestion5'),
    path('equestion6/',equestion6_form,name='equestion6'),
    path('equestion7/',equestion7_form,name='equestion7'),
    path('equestion8/',equestion8_form,name='equestion8'),
    path('documents/',documentsprepared_form,name='documents'),
    path('pre-ratings/',preRating,name='pre-ratings'),
    path('equestion9/',equestion9_form,name='equestion9'),
    path('equestion10/',equestion10_form,name='equestion10'),
    path('equestion11/',equestion11_form,name='equestion11'),
    path('equestion12/',equestion12_form,name='equestion12'),
    path('equestion13/',equestion13_form,name='equestion13'),
    path('equestion14/',equestion14_form,name='equestion14'),
    path('referral/', referral_response_view, name='referral'),
    path('lending-requiremetns/',lendig_requirements_views,name='lending-requiremetns'),
]
