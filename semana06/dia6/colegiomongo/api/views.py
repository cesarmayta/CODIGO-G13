from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Matricula
from .serializers import MatriculaSerializer

class MatriculaView(APIView):

    def get(self,request):
        dataMatricula = Matricula.objects.all()
        serMatricula = MatriculaSerializer(dataMatricula,many=True)
        return Response(serMatricula.data)

    def post(self,request):
        serMatricula = MatriculaSerializer(data=request.data)
        serMatricula.is_valid(raise_exception=True)
        serMatricula.save()

        return Response(serMatricula.data)