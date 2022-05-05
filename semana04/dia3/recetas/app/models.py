from enum import unique
from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

class Receta(models.Model):
    titulo = models.CharField(max_length=100,unique=True)
    ingredientes = models.TextField(help_text='redacta los ingredientes')
    preparacion = models.TextField()
    tiempo_registro = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(Autor,on_delete=models.RESTRICT)

class Comentario(models.Model):
    receta = models.ForeignKey(Receta,on_delete=models.CASCADE)
    texto = models.TextField(help_text='comentario')