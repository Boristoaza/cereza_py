from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Perfil(models.Model):
  nombre_usuario = models.CharField(max_length=40,blank=True,null=True)
  usuario = models.OneToOneField(User,on_delete=models.CASCADE , related_name='perfil')
  avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
  banner = models.ImageField(upload_to='banner',null=True,blank=True)
  biografia = models.TextField(max_length=250, null=True,blank=True)

  def __str__(self):
        return self.usuario.username

  def obtener_nombre(Self):
    return Self.nombre_usuario or Self.usuario.username
