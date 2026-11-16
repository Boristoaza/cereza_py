from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q
from usuario.models import Perfil


# def buscador(request):
#     if request.method == 'GET':
#         texto_busqueda = request.GET.get('busqueda')
#         buscar = Perfil.objects.filter(Q(usuario__username__icontains=texto_busqueda)|
#                                        Q(nombre_usuario__icontains=texto_busqueda))


#         contexto = { 'busqueda': buscar  }

#     return render(request,'busquedas.html', contexto)


def buscador(request):
    texto_busqueda = request.GET.get('busqueda', '').strip()

    buscar = Perfil.objects.none()

    if texto_busqueda:
        buscar = Perfil.objects.filter(
            Q(usuario__username__icontains=texto_busqueda) |
            Q(nombre_usuario__icontains=texto_busqueda)
        ).select_related('usuario')

    contexto = {
        'busqueda': buscar
    }

    return render(request, 'busquedas.html', contexto)
