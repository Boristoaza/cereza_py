from django.urls import path
from . import views

app_name = 'seguir'

urlpatterns = [
  path('seguir/', views.seguir, name='seguir'),
  path('eliminarSeguidor/',views.eliminar_seguidor , name='eliminar_seguidor'),
  path('ver_seguidos/<str:usuario>/', views.ver_seguidos, name='ver_seguidos'),
  path('ver_seguidores/<str:usuario>/', views.ver_seguidores, name='ver_seguidores'),
]
