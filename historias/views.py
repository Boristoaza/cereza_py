from django.shortcuts import render , redirect
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User

def subir_historia(request):
  if request.method == 'POST':
    archivo_historia = request.POST.get('archivo_historia')
    descripcion = request.POST.get('descripcion_historia')

  return HttpResponse('se subio con extito')