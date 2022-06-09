from rest_framework.views import APIView
from rest_framework.response import Response

class IndexView(APIView):

    def get(self,request):
        context = {
            'status':True,
            'content':'api django activa'
        }
        return Response(context)