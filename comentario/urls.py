from django.urls import path
from . import views

app_name='comentarios'

urlpatterns = [
  path('comentar/', views.comentario , name='comentar'),
  path('ver_comentarios/<int:id>/',views.ver_comentarios , name='ver_comentarios'),
]