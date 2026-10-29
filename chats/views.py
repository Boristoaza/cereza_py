from django.shortcuts import render , get_object_or_404

from seguidores.models import Follower
from django.contrib.auth.models import User
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