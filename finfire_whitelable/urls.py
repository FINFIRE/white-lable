from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from tenants.views import TenantBrandingView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/branding/', TenantBrandingView.as_view(), name='tenant-branding'),
    path('', include('registration.urls')),
    path('', include('master_review.urls')),
    path('', include('Algorithm.urls')),
    path('', include('entreprise_questions.urls')),
    path('', include('iquestions.urls')),
    path('', include('CM_Market.urls')),
    path('', include('Matching_Algorithm.urls')),
    path('', include('truth_in_capital.urls')),
    path('api/', include('connections.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
