from django.db import models

# Create your models here.



class Ropa(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='ropa_images')

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
    
