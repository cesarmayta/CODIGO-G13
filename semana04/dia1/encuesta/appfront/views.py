from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app_index(request):
    return HttpResponse('<h1>INDEX DE MI APP</h1>')

def detalle(request,pregunta_id):
    return HttpResponse('pregunta nro %s.' % pregunta_id)