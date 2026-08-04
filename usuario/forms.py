
from django import forms
from .models import Perfil


class Avatar_from(forms.ModelForm):
  class Meta:
    model  = Perfil
    fields = ['avatar']
    widgets = {
            "avatar": forms.ClearableFileInput(attrs={
                "class": "form-control-cereza",
                "accept": "image/*",
            })
        }

class Biogradia_form(forms.ModelForm):
  class Meta:
    model = Perfil
    fields = ['biografia']
