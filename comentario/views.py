from django.http import JsonResponse ,HttpResponse
from .models import Comentario
from post.models import Post
from usuario.models import Perfil
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render

def comentario(request):
    if request.method == "POST":
        comentario_texto = request.POST.get("comentar")
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




# esto es una prueba nada mas
def ver_comentarios(request ,id_post):
    consutar_comentario = Comentario.objects.filter(post_id=id_post)

    lista_comentario = []
    for i in consutar_comentario:
        lista_comentario.append(i.comentario)
    data = [{
        "id_del_post":id_post,
        "msg":"200",
        "comentarios":lista_comentario,
    }]
    return JsonResponse(data , safe=False)
