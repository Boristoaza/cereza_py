from django.db import models
from post.models import Post
from django.contrib.auth.models import User
# Create your models here.
class Comentario(models.Model):
  comentario = models.TextField(max_length=250,blank=True,null=True)
  post = models.ForeignKey(Post,on_delete=models.CASCADE)
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  fecha = models.DateTimeField(auto_now_add=True)
