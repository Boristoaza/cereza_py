
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',include('usuario.urls',namespace='usuario')),
    path('post/',include('post.urls',namespace='publicacion')),
    path('reacciones/',include('reacciones.urls',namespace='reacciones')),
    path('comentarios/', include('comentario.urls',namespace='comenatirios')),
    path('feed/',include('feed.urls',namespace='feed')),
    path('buscar/',include('buscador.urls',namespace='buscador')),
    path('seguir/',include('seguidores.urls',namespace='seguir')),
    path('chat/',include('chats.urls',namespace='chat')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
] + static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
