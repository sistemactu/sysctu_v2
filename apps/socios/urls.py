from django.urls import path, URLPattern
from .views import agregarsocio, socio_list, solic_list, socio_edit, socio_detail

urlpatterns = [
    path('', socio_list, name='listar_socios'),
    path('nueva_solicitud/', agregarsocio, name='nueva_solicitud'),
    path('solicitudes/', solic_list, name='listar_solicitudes'),
    path('editar/<int:pk>/', socio_edit, name='editar_socio'),
    path('detalle/<int:pk>/', socio_detail, name='detalle_socio'),
]
