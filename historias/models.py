from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Historias(models.Model):
  file_historia = models.ImageField(upload_to='historia')
  descripcion = models.TextField(max_length=100,blank=True,null=True)
  fecha_creacion = models.DateTimeField(auto_now_add=True)
  fecha_expiracion = models.DateTimeField()
