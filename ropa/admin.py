from django.contrib import admin
from ropa.models import Ropa

# Register your models here.

@admin.register(Ropa)
class RopaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "precio")

