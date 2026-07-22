from django.http import JsonResponse
from .models import Comentario
from post.models import Post
from usuario.models import Perfil
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render



def comentario(request):

    if request.method == "POST":

        comentario_texto = request.POST.get("comentario")
        id_post = request.POST.get("id_post")

        if comentario_texto and id_post:

            post = Post.objects.get(id=id_post)

            crear_comentario = Comentario.objects.create(
                usuario=request.user,
                post=post,
                comentario=comentario_texto
            )

            nombre_usuario = Perfil.objects.get(usuario=request.user)

            return JsonResponse({
                "estado": "ok",
                "usuario": nombre_usuario,
                "comentario": crear_comentario.comentario,
                "post": post.id,
                "fecha": crear_comentario.fecha.strftime("%d/%m/%Y %H:%M")
            })

        return JsonResponse({
            "estado": "error",
            "mensaje": "Datos inválidos"
        }, status=400)

    return JsonResponse({
        "estado": "error",
        "mensaje": "Método no permitido"
    }, status=405)

def ver_comentarios(request):
    if request.method == "GET":
        id_post = request.GET.get('id')
        print(id_post)
    return render(request,'feed.html')
