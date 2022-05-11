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

@api_view(['POST'])
def setAlumno(request):
    serAlumno = AlumnoSerializer(data=request.data)
    serAlumno.is_valid(raise_exception=True)

    nuevoAlumno = serAlumno.save()

    context = {
        'status':'ok',
        'message':'alumno creado',
        'data':AlumnoSerializer(nuevoAlumno).data
    }

    return Response(context)

######### ENDPOINTS PROFESOR
from .models import Profesor
from .serializers import ProfesorSerializer

@api_view(['GET','POST'])
def profesor(request):
    if request.method == 'GET':
        lstProfesores = Profesor.objects.all()
        serProfesores = ProfesorSerializer(lstProfesores,many=True)
        
        return Response(serProfesores.data)

    elif request.method == 'POST':
        serProfesor = ProfesorSerializer(data=request.data)
        if serProfesor.is_valid():
            serProfesor.save()
            return Response(serProfesor.data)
        else:
            return Response(serProfesor.errors)

@api_view(['GET','PUT','DELETE'])
def profesor_detail(request,profesor_id):
    objProfesor = Profesor.objects.get(id=profesor_id)

    if request.method == 'GET':
        serProfesor = ProfesorSerializer(objProfesor)
        return Response(serProfesor.data)

    elif request.method=='PUT':
        serProfesor = ProfesorSerializer(objProfesor,data=request.data)
        if serProfesor.is_valid():
            serProfesor.save()
            return Response(serProfesor.data)
        else:
            return Response(serProfesor.errors)
    elif request.method == 'DELETE':
        objProfesor.delete()
        return Response(status=204)