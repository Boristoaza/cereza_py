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

  # post = Post.objects.select_related('usuario')\
  #   .prefetch_related('reaccion_set', 'pack_set', 'comentario_set')\
  #   .order_by('-fecha')

  post = Post.objects.filter(usuario=request.user).select_related('usuario__perfil').prefetch_related('pack_set')
  for i in post:
      if i.post_original:
          print("Post compartido:", i.id)
          print("Original:", i.post_original.id)

          for x in i.post_original.pack_set.all():
              print(x.imagen)

  consultar_post = Post.objects.get(id=17)





  return render(
      request,
      'feed.html',
      {
          'seguidos': seguidos,
          'post':post
      }
  )
