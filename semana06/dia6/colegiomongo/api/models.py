from unittest.util import _MAX_LENGTH
from djongo import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()

    class Meta:
        abstract = True

class Curso(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        abstract = True

class Matricula(models.Model):
    nro = models.CharField(max_length=20)
    alumno = models.EmbeddedField(model_container=Alumno,null=False,blank=False)
    cursos = models.ArrayField(
        model_container=Curso,null=True,blank=True
    )