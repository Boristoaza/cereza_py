from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login
from django.contrib.auth import logout
from post.models import Post,Pack
from .models import Perfil
from django.http import HttpResponse , JsonResponse
from django.shortcuts import get_object_or_404, render
from reacciones.models import Reaccion
from seguidores.models import Follower
from .forms import Avatar_from , Biogradia_form

def registro_view(request):
    if request.user.is_authenticated:
        return redirect('usuario:perfil')

    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuerio')
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        if User.objects.filter(username=nombre_usuario).exists():
            return render(request, 'registro.html', {
                'msg': 'Ese nombre de usuario ya existe.'
            })

        if User.objects.filter(email=correo).exists():
            return render(request, 'registro.html', {
                'msg': 'Ese correo ya está registrado.'
            })

        crear_usuario = User.objects.create_user(
            username=nombre_usuario,
            email=correo,
            password=password
        )

        login(request, crear_usuario)
        return redirect('usuario:perfil')

    return render(request, 'registro.html')



def login_view(request):
  if request.user.is_authenticated:
        return redirect('usuario:perfil')
  if request.method == 'POST':
    correo = request.POST.get('nombre')
    password = request.POST.get('password')
    username = User.objects.filter(email=correo).values_list('username', flat=True).first() 
    usuario = authenticate(username=username,password=password)
    if usuario is not None:
       login(request,usuario)
       return redirect('usuario:perfil')
  return render(request,'login.html')

def logout_view(request):
  logout(request)
  return redirect('usuario:login')


def main_view(request):
    if request.user.is_authenticated:
        return redirect('usuario:perfil')
    else:
        return redirect('usuario:login')

@login_required
def perfil_view(request):
    # Obtiene el perfil o lo crea si es la primera vez
    perfil, created = Perfil.objects.get_or_create(
        usuario=request.user
    )

    if request.method == 'POST':
        avatar = request.FILES.get('avatar')
        banner = request.FILES.get('banner')
        biografia = request.POST.get('biografia')

        # Solo reemplaza las imágenes si el usuario subió nuevas
        if avatar:
            perfil.avatar = avatar

        if banner:
            perfil.banner = banner

        if biografia is not None:
            perfil.biografia = biografia

        perfil.save()
    # actaulizar avatar
    if request.method == 'POST':
        formulario = Avatar_from(
            request.POST,
            request.FILES,
            instance=perfil
        )
        if formulario.is_valid():
            formulario.save()
    else:
        formulario = Avatar_from(instance=perfil)

    repost = ""
    tab = "1"

    if request.method == "POST":
        usuario = request.POST.get("nombre_usuario")
        tab_nombre = request.POST.get("tab_op")

        tab = tab_nombre

        if usuario and tab_nombre == "2":
            # Repost
            usuario_filtro = User.objects.get(username=usuario)

            repost = Post.objects.filter(
                usuario=usuario_filtro,
                post_original__isnull=False
            ).select_related(
                "usuario",
                "post_original",
                "post_original__usuario"
            ).prefetch_related(
                "post_original__pack_set"
            )

        elif usuario and tab_nombre == "3":
            # Guardados
            print("-> tab guardados")

    # descripcion
    if request.method == 'POST':
        biografia = Biogradia_form(request.POST, instance=perfil)
        if biografia.is_valid():
            biografia.save()
    else:
        biografia = Biogradia_form(instance=perfil)


    seguidos = (
        Follower.objects
        .filter(seguidor=request.user)
        .select_related('seguido__perfil')
    )

    seguidores = (
        Follower.objects
        .filter(seguido=request.user)
        .select_related('seguidor__perfil')
    )

    cantidad_seguidores = seguidores.count()
    cantidad_seguidos = seguidos.count()

    publicaciones = (
        Post.objects
        .filter(
            usuario=request.user,
            post_original__isnull=True
        )
        .select_related(
            'usuario',
            'usuario__perfil'
        )
        .prefetch_related(
            'pack_set',
            'comentario_set',
            'reaccion_set'
        )
        .order_by('-id')
    )

    contexto = {
        'perfil': perfil,
        'formulario':formulario,
        'biografia':biografia,
        'posts': publicaciones,
        'seguidos': seguidos,
        'seguidores': seguidores,
        'cantidad_seguidores': cantidad_seguidores,
        'cantidas_seguidos': cantidad_seguidos,
        'repost':repost,
        'tab':tab
    }

    return render(request, 'perfil.html', contexto)

@login_required
def ver_perfil(request, usuario):
    from django.db.models import Q
    # este es un buscador de usuarios
    perfil = get_object_or_404(
        Perfil,
        Q(nombre_usuario=usuario) |
        Q(usuario__username=usuario)
    )

    seguidos = (
        Follower.objects
        .filter(seguidor=perfil.usuario)
        .select_related('seguido__perfil')
    )

    seguidores = (
        Follower.objects
        .filter(seguido=perfil.usuario)
        .select_related('seguidor__perfil')
    )

    # comprobar seguidor
    verificar_seguidor = Follower.objects.filter(
        seguidor_id=request.user.id,
        seguido_id=perfil.usuario.id
    ).exists()

    # cuenta los seguidores
    cantidad_seguidores = seguidores.count()
    cantidad_seguidos = seguidos.count()


    # treae los post del usuario que se

    posts = (
        Post.objects.filter(usuario=perfil.usuario)
        .select_related('usuario', 'usuario__perfil')
        .prefetch_related(
            'comentario_set',
            'reaccion_set',
            'pack_set',
        )
    ).order_by('-id')


    contexto = {
        'follow':verificar_seguidor,
        'perfil': perfil,
        'posts': posts,
        'seguidos': seguidos,
        'seguidores': seguidores,
        'cantidad_seguidores': cantidad_seguidores,
        'cantidad_seguidos': cantidad_seguidos,
    }

    return render(request, 'perfil.html', contexto)


@login_required
def tabs(request, id):
    print(id)

    # if id == 2:

    #     usuario = request.user

    #     repost = (
    #         Post.objects
    #         .filter(
    #             usuario=usuario,
    #             post_original__isnull=False
    #         )
    #         .select_related(
    #             'usuario',
    #             'usuario__perfil',
    #             'post_original',
    #             'post_original__usuario',
    #             'post_original__usuario__perfil'
    #         )
    #         .prefetch_related(
    #             'post_original__pack_set'
    #         )
    #         .order_by('-id')
    #     )

    #     return render(
    #         request,
    #         'post_grid.html',
    #         {
    #             'repost': repost
    #         }
    #     )

    return redirect('usuario:perfil')