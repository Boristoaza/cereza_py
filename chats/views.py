from django.shortcuts import render , get_object_or_404

from seguidores.models import Follower
from django.contrib.auth.models import User
from .models import Mensaje , Conversacion

def index(request):
    amigos = Follower.objects.filter(seguidor=request.user)
    for i in amigos:
        print(i.id)

    contexto = {'seguidos':amigos}
    return render(request, "chat/index.html",contexto)




def room(request, room_name):

    amigo = get_object_or_404(
        Follower,
        seguidor=request.user,
        seguido__username=room_name
    )

    usuario1 = request.user.id
    usuario2 = amigo.seguido.id

    nombre_sala = '_'.join(map(str, sorted([usuario1, usuario2])))

    return render(request, "chat/room.html", {
        "room_name": nombre_sala
    })


def chat_view(request):

    amigos = Follower.objects.filter(seguidor=request.user)

    lista_amigos = []
    mensajes = []

    nombre_chat = request.GET.get('sala')

    for amigo in amigos:

        usuario1 = request.user.id
        usuario2 = amigo.seguido.id

        nombre_sala = '_'.join(map(str, sorted([usuario1, usuario2])))

        conversacion, creada = Conversacion.objects.get_or_create(
            usuario1_id=min(usuario1, usuario2),
            usuario2_id=max(usuario1, usuario2)
        )

        lista_amigos.append({
            'usuario': amigo.seguido.username.strip(),
            'nombre_sala': nombre_sala
        })

        if nombre_chat == nombre_sala:
            mensajes = Mensaje.objects.filter(
                conversacion=conversacion
            ).order_by('fecha_envio')

    contexto = {
        'seguidos': lista_amigos,
        'mensajes': mensajes
    }

    return render(request, 'chat/chat.html', contexto)