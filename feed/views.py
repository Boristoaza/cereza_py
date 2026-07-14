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
  ).values_list('seguido_id', flat=True)

  seguidos = User.objects.filter(id__in=ids_seguidos).select_related('perfil')
  posts = (
        Post.objects.filter(usuario_id__in=ids_seguidos)
        .select_related('usuario', 'usuario__perfil')
        .prefetch_related('pack_set')
    )

#   for post in posts:
#     for imagen in post.pack_set.all():
#         print(
#             post.usuario.perfil.nombre_usuario,
#             post.descripcion,
#             post.fecha,
#             imagen.imagen
#         )



  post = Post.objects.select_related('usuario')\
    .prefetch_related('reaccion_set', 'pack_set', 'comentario_set')\
    .order_by('-fecha')




  return render(
      request,
      'feed.html',
      {
          'seguidos': seguidos,
          'post':post
      }
  )
