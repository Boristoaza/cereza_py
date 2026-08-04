from django import forms
from .models import Post , Pack

class CrearPost_form(forms.models):
  class Meta:
    model = Post
    fields = ['usuario','descripcion']

class Post_pack_form(forms.models):
  class Meta:
    model = Pack
    fields = ['imagen']
