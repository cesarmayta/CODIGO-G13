from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('alumnos',views.alumnos),
    path('home',views.home),
    path('getalumno',views.getAlumnos),
    path('setalumno',views.setAlumno)
]