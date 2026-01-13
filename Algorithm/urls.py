from django.urls import path, include
from .views import capital_viewt,fetch_capital_data,algorithmInsightDashboard
#Views for the urls
urlpatterns = [
    path('algorithmmatrixA/',capital_viewt,name='capitalview'),
    path('fetch-capital-data/', fetch_capital_data, name='fetch_capital_data'),
    path('all-percentage/',algorithmInsightDashboard,name='all_percentage')
]