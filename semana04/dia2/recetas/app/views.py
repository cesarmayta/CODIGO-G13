from django.shortcuts import render,redirect

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

def registrarReceta(request):
    frmReceta = RecetaForm(request.POST)
    if frmReceta.is_valid():
        dataReceta = frmReceta.cleaned_data
        print(dataReceta)
        #insertamos la receta en la tabla
        nuevaReceta = Receta()
        nuevaReceta.titulo = dataReceta['titulo']
        nuevaReceta.ingredientes = dataReceta['ingredientes']
        nuevaReceta.preparacion = dataReceta['preparacion']
        nuevaReceta.autor = dataReceta['autor']
        nuevaReceta.save()
        
    return redirect('/')
