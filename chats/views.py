from django.shortcuts import render

from seguidores.models import Follower

def index(request):
    amigos = Follower.objects.all()
    print(amigos)
    for i in amigos:
        print(i.seguido)
    contexto = {'seguidos':amigos}
    print(contexto)
    return render(request, "chat/index.html",contexto)

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})