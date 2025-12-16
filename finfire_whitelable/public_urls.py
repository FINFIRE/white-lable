from django.contrib import admin

from rest_framework import generics, response, status
from rest_framework.permissions import AllowAny

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

class BackendHealthCheckApiView(generics.GenericAPIView):
    http_method_names = ['get']
    permission_classes = [AllowAny, ]

    def get(self, request, *args, **kwargs):
        return response.Response({'success': 'Backend Working'}, status=status.HTTP_200_OK)


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('tenants/', include('tenants.urls')),
    path('api/health-check/', BackendHealthCheckApiView.as_view(), name='backend-health-check'),

]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


