from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.contrib.auth.models import User
from .models import Follower
from django.shortcuts import redirect
from usuario.models import Perfil





def seguir(request):
    if request.method == 'POST':

        usuario_a_seguir = request.POST.get("usuario")

        seguido = User.objects.filter(
            username=usuario_a_seguir
        ).get()

        consultar_seguidor = Follower.objects.filter(
            seguidor=request.user,
            seguido=seguido
        ).exists()

        print(seguido, consultar_seguidor)

        if consultar_seguidor == True:

            print("estás siguiendo a esta persona")

            borrar_follow = Follower.objects.filter(
                seguidor=request.user,
                seguido=seguido
            ).delete()

            print(f"se eliminó {borrar_follow}")

        else:

            crear_follow = Follower.objects.create(
                seguidor=request.user,
                seguido=seguido
            )

            print(f"se creó el seguimiento {crear_follow}")

        datos = [{
            "usuario": usuario_a_seguir
        }]

        return JsonResponse(datos, safe=False)

    return JsonResponse({
        "error": "Método no permitido"
    }, status=405)


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