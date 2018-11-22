from django.urls import path, URLPattern
from .views import agregarsocio, socio_list

urlpatterns = [
    path('', socio_list, name='listar_socios'),
    path('nueva_solicitud/', agregarsocio, name='agregarsocio'),
]
