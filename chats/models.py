from django.db import models
from django.contrib.auth.models import User


class Conversacion(models.Model):
    usuario1 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='conversaciones_usuario1'
    )

    usuario2 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='conversaciones_usuario2'
    )

    class Meta:
        verbose_name_plural = 'Conversaciones'

    fecha_creacion = models.DateTimeField(auto_now_add=True)


class Mensaje(models.Model):
    conversacion = models.ForeignKey(
        Conversacion,
        on_delete=models.CASCADE,
        related_name='mensajes'
    )

    emisor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    contenido = models.TextField()

    fecha_envio = models.DateTimeField(auto_now_add=True)