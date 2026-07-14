from django.urls import path
from . import views

app_name = 'buscador'

urlpatterns = [
  path('buscar/', views.buscador , name='buscar')
]