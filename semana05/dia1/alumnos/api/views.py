from django.http import JsonResponse

#### para trabajar con rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Alumno

from .serializers import AlumnoSerializer

def index(request):
    return JsonResponse({
        'mensaje':'Bienvenido a mi Api'
    })

@api_view(['GET'])
def home(request):
    return Response({
        'status':'ok',
        'message':'hola mundo desde drf'
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

@api_view(['GET'])
def getAlumnos(request):
    lstAlumnos = Alumno.objects.all()
    serAlumnos = AlumnoSerializer(lstAlumnos,many=True)

    context = {
        'status':'ok',
        'data':serAlumnos.data
    }
    return Response(context)

