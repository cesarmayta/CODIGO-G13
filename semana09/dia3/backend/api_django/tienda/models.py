from django.db import models

from cloudinary.models import CloudinaryField

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = CloudinaryField('image',default='')
    precio = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre