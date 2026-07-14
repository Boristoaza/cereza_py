from django.urls import path
from . import views

app_name = 'reacciones'

urlpatterns = [
   path('like/', views.reaccion_like , name='like')
]
