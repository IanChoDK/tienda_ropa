from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ropa, Producto 

class RegistroForm(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    password = forms.CharField(label="Contrasenia", widget=forms.PasswordInput)

class RopaForm(forms.ModelForm):
    class Meta:
        model = Ropa
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'disponible', 'categoria']

# shop/forms.py
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['ropa', 'talle', 'color', 'stock']
        