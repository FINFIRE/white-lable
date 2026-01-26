from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('registration.urls')),
    path('matching-algorithm/', include('Matching_Algorithm.urls')),
    path('iquestions/', include('iquestions.urls')),
    path('cm-market/', include('CM_Market.urls')),
    path('entreprise-questions/', include('entreprise_questions.urls')),
    path('connections/', include('connections.urls')),
    path('master-review/', include('master_review.urls')),
    path('truth-in-capital/', include('truth_in_capital.urls')),



]




urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
