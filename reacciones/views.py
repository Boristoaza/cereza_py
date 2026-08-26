from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import Reaccion
from django.contrib.auth.models import User
from post.models import Post

def reaccion_like(request):
    if request.method == "POST":
        like = request.POST.get("id_post_like")
        usuario = request.user.id

        buscar_post = Post.objects.get(id=like)

        verificar_reaccion = Reaccion.objects.filter(
            post_id=buscar_post,
            usuario_id=usuario
        ).exists()

        if verificar_reaccion == True:
            borrar_reaccion = Reaccion.objects.filter(
                post_id=buscar_post,
                usuario_id=usuario
            ).delete()

            print(f"Existe esta reacción, por lo tanto hay que borrarla: {borrar_reaccion}")

        else:
            crear_reaccion = Reaccion.objects.create(
                post_id=buscar_post.id,
                usuario_id=usuario
            )

            print(f"Esta reacción se debe crear: {crear_reaccion}")

        datos = [{
            "like": like,
            "usuario": usuario,
        }]

        return JsonResponse(datos, safe=False)
