from django.urls import path
from . import views


urlpatterns = [
    path('nueva/', views.acta_new, name='nueva_acta'),
]
