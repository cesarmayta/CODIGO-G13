from rest_framework import serializers

from .models import (
    Mesa,Categoria,Plato
)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = '__all__'

class CategoriaPlatosSerializer(serializers.ModelSerializer):
    Platos = PlatoSerializer(many=True,read_only=True)
    class Meta:
        model = Categoria
        fields = ['categoria_id','categoria_nom','Platos']