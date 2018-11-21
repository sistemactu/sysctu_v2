from django.urls import path
from . import views


urlpatterns = [
    path('', views.acta_list, name='actas'),
    path('nueva/', views.acta_new, name='nueva_acta'),
    path('detalle/<int:pk>/', views.acta_detail, name='detalle_acta'),
    path('editar/<int:pk>/', views.acta_edit, name='editar_acta'),
    path('eliminar/', views.acta_delete, name='eliminar_acta'),
]
