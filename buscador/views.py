from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q
from usuario.models import Perfil


def buscador(request):
    if request.method == 'GET':
        texto_busqueda = request.GET.get('busqueda')
        buscar = Perfil.objects.filter(Q(usuario__username__icontains=texto_busqueda)|
                                       Q(nombre_usuario__icontains=texto_busqueda))



        for i in buscar:
            # img_perfil = i.avatar
            # return img_perfil
            # print(i.avatar)
            # print(i.id)
            print(i.usuario)
            # print(i.biografia)


        contexto = { 'busqueda': buscar  }

    return render(request,'busquedas.html', contexto)