from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    password = forms.CharField(label="Contrasenia", widget=forms.PasswordInput)
from .models import Ropa

class RopaForm(forms.ModelForm):
    class Meta:
        model = Ropa
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'stock', 'disponible', 'categoria']
