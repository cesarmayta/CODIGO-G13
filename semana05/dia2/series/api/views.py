from rest_framework.views import APIView
from rest_framework.response import Response

class IndexView(APIView):

    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)