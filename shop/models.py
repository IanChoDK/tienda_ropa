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
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='ropa')
    activo = models.BooleanField(default=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'ropa'
        verbose_name_plural = 'ropas'

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
    

class Talle(models.Model):
    nombre = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'talle'
        verbose_name_plural = 'talles'

    def __str__(self):
        return self.nombre

class Color(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colores'

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    ropa = models.ForeignKey(Ropa, on_delete=models.CASCADE, related_name='productos')
    talle = models.ForeignKey(Talle, on_delete=models.CASCADE, related_name='talle')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='color')
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return f"{self.ropa.nombre} - {self.talle.nombre} - {self.color.nombre}"