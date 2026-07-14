from django.shortcuts import render
from django.shortcuts import redirect
from .models import Reaccion
from django.contrib.auth.models import User
from post.models import Post


# Create your views here.

def reaccion_like(request):
    if request.method == 'POST':
        post_id = request.POST.get('id_post')

        try:
            post = Post.objects.get(id=post_id)

            reaccion, creada = Reaccion.objects.get_or_create(
                usuario=request.user,
                post=post
            )

            if not creada:
                reaccion.delete()

        except Post.DoesNotExist:
            pass

    return redirect('usuario:perfil')
