from django.shortcuts import render

from .models import Categoria,Producto

# Create your views here.
def index(request):
    listaProductos = Producto.objects.all()
    context = {
        'productos':listaProductos
    }
    return render(request,'index.html',context)
