from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Matricula
from .serializers import MatriculaSerializer

class MatriculaView(APIView):

    def get(self,request):
        dataMatricula = Matricula.objects.all()
        serMatricula = MatriculaSerializer(dataMatricula,many=True)
        return Response(serMatricula.data)