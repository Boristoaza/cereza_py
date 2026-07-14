from django.urls import path
from . import views

app_name = 'seguir'

urlpatterns = [
  path('seguir/', views.seguir, name='seguir'),
  path('eliminarSeguidor/',views.eliminar_seguidor , name='eliminar_seguidor'),
]