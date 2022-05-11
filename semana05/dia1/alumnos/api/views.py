from django.http import JsonResponse

from .models import Alumno

def index(request):
    return JsonResponse({
        'mensaje':'Bienvenido a mi Api'
    })

def alumnos(request):
    dataAlumnos = Alumno.objects.all()
    lstAlumnos = []
    for alumno in dataAlumnos:
        dicAlumno = {
            'nombre': alumno.nombre,
            'email':alumno.email
        }
        lstAlumnos.append(dicAlumno)

    context = {
        'status':'ok',
        'data': lstAlumnos
    }
    
    return JsonResponse(context)
