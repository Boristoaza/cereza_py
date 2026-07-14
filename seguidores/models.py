from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Follower(models.Model):
    seguidor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='siguiendo'
    )

    seguido = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='seguidores'
    )
    def __str__(self):
      return f"{self.seguidor.username} sigue a {self.seguido.username}"
