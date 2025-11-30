"""
URL de configuration pour le projet concess_api.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('concession.urls')),
]

