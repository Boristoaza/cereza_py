# from django.db import models
# from django.contrib.auth.models import User


# # Create your models here.
# class Avatar(models.Model):
#   usuario = models.ForeignKey(User,on_delete=models.CASCADE)
#   avatar = models.ImageField(upload_to='avatar')
#   fecha = models.DateField(auto_now_add=True)


# class Banner(models.Model):
#   usuario = models.ForeignKey(User,on_delete=models.CASCADE)
#   banner = models.ImageField(upload_to='banner')
#   fecha = models.DateField(auto_now_add=True)

# class Post(models.Model):
#   usuario = models.ForeignKey(User,on_delete=models.CASCADE)
#   banner = models.ImageField(upload_to='post')
#   fecha = models.DateField(auto_now_add=True)

# class Historias(models.Model):
#   usuario = models.ForeignKey(User,on_delete=models.CASCADE)
#   banner = models.ImageField(upload_to='historias')
#   fecha = models.DateField(auto_now_add=True)
