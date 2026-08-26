from django.shortcuts import render
from django.contrib.auth.models  import User
from seguidores.models import Follower
from post.models import Post , Pack
from reacciones.models import Reaccion
from comentario.models import Comentario
from usuario.models import Perfil

def feed_view(request):

    ids_seguidos = Follower.objects.filter(
        seguidor=request.user
    ).values_list(
        'seguido_id',
        flat=True
    )

    usuarios_feed = list(ids_seguidos) + [request.user.id]

    posts = (
        Post.objects
        .filter(usuario_id__in=usuarios_feed)
        .select_related(
            'usuario',
            'usuario__perfil'
        )
        .prefetch_related(
            'pack_set'
        )
        .order_by('-fecha','-id')[:10]
    )

    return render(
        request,
        'feed.html',
        {
            'post': posts
        }
    )

def explorer_view(request):

    if request.method == "POST":

        usuario = request.POST.get("usuario")


        publicaciones = (
            Post.objects
            .all()
            .prefetch_related("pack_set")
            .order_by("-id")
        )

        print(f"-> explorer {usuario}")

        return render(
            request,
            "explorar.html",
            {
                "publicaciones": publicaciones
            }
        )

    return render(request, "explorar.html")