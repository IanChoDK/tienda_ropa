from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre



class Ropa(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='ropa_images')
    stock = models.IntegerField(default=0)
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='ropa')

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
    
