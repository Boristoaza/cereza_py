from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
   usuario = models.ForeignKey(User,on_delete=models.CASCADE)
   descripcion = models.TextField(max_length=200,blank=True)
   fecha = models.DateField(auto_now_add=True)
   post_original = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='compartidos'
    )


class Pack(models.Model):
   post = models.ForeignKey(Post,on_delete=models.CASCADE)
   imagen = models.ImageField(upload_to='post/imagen', null=True,blank=True)
   video = models.FileField(upload_to='post/video', null=True , blank=True)
