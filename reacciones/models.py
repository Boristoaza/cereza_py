from django.db import models
from django.contrib.auth.models import User
from post.models import Post
# Create your models here.
class Reaccion(models.Model):
  usuario = models.ForeignKey(User,on_delete=models.CASCADE)
  post = models.ForeignKey(Post,on_delete=models.CASCADE)
