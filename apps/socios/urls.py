from django.urls import path, URLPattern
from apps.socios.views import agregarsocio

urlpatterns = [
    path('', agregarsocio, name='agregarsocio'),
]
