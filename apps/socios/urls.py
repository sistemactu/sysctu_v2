from django.urls import path, URLPattern
from .views import agregarsocio, socio_list, solic_list

urlpatterns = [
    path('', socio_list, name='listar_socios'),
    path('nueva_solicitud/', agregarsocio, name='nueva_solicitud'),
    path('solicitudes/', solic_list, name='listar_solicitudes'),
]
