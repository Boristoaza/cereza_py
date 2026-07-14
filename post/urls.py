from django.urls import path
from . import views


app_name = 'publicacion'

urlpatterns = [
  path('publicar/',views.publicacion,name='publicar'),
  path('compartir_post',views.compartir_publicacion,name='compartir_post')
]