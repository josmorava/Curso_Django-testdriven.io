"""
URLS drf_proyect
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path

from .views import ping

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', ping, name="ping")
]
