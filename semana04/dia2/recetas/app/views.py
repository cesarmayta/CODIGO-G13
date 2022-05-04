from django.shortcuts import render

from .models import Receta
from .forms import RecetaForm

# Create your views here.
def index(request):
    listaRecetas = Receta.objects.all()
    print(listaRecetas)

    #formulario de nueva receta
    frmReceta = RecetaForm()
    context = {
        'frmReceta':frmReceta,
        'recetas':listaRecetas
    }
    return render(request,'index.html',context)