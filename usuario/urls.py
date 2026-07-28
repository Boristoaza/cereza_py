from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
  path('',views.main_view , name='main'),
  path('perfil/',views.perfil_view,name='perfil'),
  path('login/',views.login_view,name='login'),
  # path('ver_perfil/<int:id>', views.ver_perfil ,name='ver_perfil'),
  path('ver_perfil/<str:usuario>', views.ver_perfil ,name='ver_perfil'),

  path('registro/',views.registro_view,name='registro'),
  path('logout/',views.logout_view,name='logout'),
]