from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.contrib.auth.models import User
from .models import Follower
from django.shortcuts import redirect
from usuario.models import Perfil


# Create your views here.
def seguir(request):
  if request.method == 'POST':
    usuerio = request.POST.get('usuario')
    verificar_usuario = User.objects.filter(username=usuerio).first()

    if verificar_usuario :
     seguir_usuario = Follower.objects.create(seguidor=request.user,seguido=verificar_usuario)
     seguidos = Follower.objects.all().values_list('seguidos')
    #  return redirect('usuario:perfil')

     print(f'seguidos {seguidos}')
    else:
      print("No existe el usuario")

    return HttpResponse(f'este es el id ')
  return HttpResponse('esto esel de seguir')


def eliminar_seguidor(resquest):
  if resquest.method == 'POST':
    id_usuerio = resquest.POST.get('id_usuario')
    return HttpResponse('hastad vales verga')
  return HttpResponse('esto esel de seguir')

def ver_seguidos(request, usuario):
    # consultar_usuario = User.objects.get(username=usuario)
    consultar_usuario2 = Perfil.objects.get(nombre_usuario=usuario)
    # print(co)


    # Usuarios que este usuario sigue
    seguidos = Follower.objects.filter(
        seguidor=consultar_usuario2.usuario
    )

    seguidos_ids = seguidos.values_list(
        "seguido_id",
        flat=True
    )

    perfiles = Perfil.objects.select_related("usuario").filter(
        usuario_id__in=seguidos_ids
    )

    lista_seguidos = []

    for perfil in perfiles:
        lista_seguidos.append({
            "nombre_usuario": perfil.nombre_usuario,
            "username": perfil.usuario.username,
            "avatar":perfil.avatar.name,
        })

    return JsonResponse(lista_seguidos, safe=False)


def ver_seguidores(request, usuario):
    consultar_usuario = Perfil.objects.get(nombre_usuario=usuario)
    # Usuarios que siguen a 'consultar_usuario'
    seguidores = Follower.objects.filter(seguido_id=consultar_usuario.id)

    seguidores_ids = seguidores.values_list("seguidor_id", flat=True)

    perfiles = Perfil.objects.select_related("usuario").filter(
        usuario_id__in=seguidores_ids
    )

    lista_seguidores = []

    for perfil in perfiles:
        lista_seguidores.append({
            "nombre_usuario": perfil.nombre_usuario,
            "username": perfil.usuario.username,
            "avatar": perfil.avatar.name,
        })

    return JsonResponse(lista_seguidores, safe=False)