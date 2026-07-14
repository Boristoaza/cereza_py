from django.urls import path
from . import views

app_name='comentarios'

urlpatterns = [
  path('comentar/', views.comentario , name='comentar')
]