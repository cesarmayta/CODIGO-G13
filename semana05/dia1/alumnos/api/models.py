from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    
