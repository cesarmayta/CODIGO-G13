from django.db import models

# Create your models here.
class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    ingredientes = models.TextField(help_text='redacta los ingredientes')
    preparacion = models.TextField()
    autor = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo