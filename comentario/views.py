from django.http import HttpResponse
from .models import Comentario
from post.models import Post
from django.shortcuts import redirect

def comentario(request):
    if request.method == "POST":
        comentario_texto = request.POST.get('comentario')
        id_post = request.POST.get('id_post')

        if comentario_texto and id_post:
            post = Post.objects.get(id=id_post)
            crear_comentario = Comentario.objects.create(usuario=request.user,post=post,comentario=comentario_texto)
            return redirect('usuario:perfil')
        else:
            return HttpResponse("no se pudo crear este comentario")

    return HttpResponse("OK")


# def ver_comentarios(resquest):
