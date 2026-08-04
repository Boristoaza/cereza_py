from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Follower
from django.shortcuts import redirect

# Create your views here.
def seguir(request):
  if request.method == 'POST':
    usuerio = request.POST.get('usuario')
    verificar_usuario = User.objects.filter(username=usuerio).first()

    if verificar_usuario :
     seguir_usuario = Follower.objects.create(seguidor=request.user,seguido=verificar_usuario)
     seguidos = Follower.objects.all().values_list('seguidos')
    #  return redirect('usuario:perfil')

     print(f'seguidos {seguidos}')
    else:
      print("No existe el usuario")

    return HttpResponse(f'este es el id ')
  return HttpResponse('esto esel de seguir')


def eliminar_seguidor(resquest):
  if resquest.method == 'POST':
    id_usuerio = resquest.POST.get('id_usuario')
    return HttpResponse('hastad vales verga')
  return HttpResponse('esto esel de seguir')


def ver_seguidos(request, usuario):
    print(usuario)
    return redirect('usuario:perfil')