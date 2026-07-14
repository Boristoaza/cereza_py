from django.http import HttpResponse
from .models import Post, Pack
from django.shortcuts import redirect


def publicacion(request):
    if request.method == 'POST':
        imagenes = request.FILES.getlist('publicacion')
        descripcion = request.POST.get('descripcion', '')

        if len(imagenes) > 10:
            return HttpResponse("Máximo 10 imágenes por publicación")

        post = Post.objects.create(
            usuario=request.user,
            descripcion=descripcion
        )

        for img in imagenes:
            Pack.objects.create(
                post=post,
                imagen=img
            )

        return redirect('usuario:perfil')

    return HttpResponse("Método no permitido")


def compartir_publicacion(request):
    if request.method == 'POST':
        id_post = request.POST.get('id_post')
        descripcion = request.POST.get('comentario_compartir')

        verificar_post = Post.objects.get(id=id_post)

        Post.objects.create(
            usuario=request.user,
            descripcion=descripcion,
            post_original=verificar_post
        )

        return HttpResponse('Compartido con éxito')