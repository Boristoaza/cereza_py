from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    # path('chat',views.chat_view ,name='chat'),
    path("chat", views.index, name="index"),
    path("<str:room_name>/",views.room,name="room" ),


    path('', views.chat_view, name='mensajes'),
    path('chat/<str:nombre_chat>/', views.chat_view, name='conversacion'),

]