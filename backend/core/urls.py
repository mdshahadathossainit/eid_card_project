from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.views.static import serve
import os

def home(request):
    return HttpResponse("Eid Card Generator Backend is Running. Use /api/generate/ for POST requests.")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('generator.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT}),
]
