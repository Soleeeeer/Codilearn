from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_root(request):
    return redirect('/api/courses/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root),
    path('api/users/', include('apps.users.urls')),
    path('api/', include('apps.courses.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
