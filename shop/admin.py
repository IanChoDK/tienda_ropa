from django.contrib import admin
from .models import Ropa, Categoria, Talle, Color, Producto

# Register your models here.
@admin.register(Ropa)
class RopaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria')
    search_fields = ('nombre',)
    list_filter = ('categoria',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Talle)
class TalleAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('ropa','talle','color')
    search_fields = ('ropa',)
    list_filter = ('talle','color',)
