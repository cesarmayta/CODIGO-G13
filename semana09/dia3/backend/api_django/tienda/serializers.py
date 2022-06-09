from dataclasses import field, fields
from rest_framework import serializers

from .models import Categoria,Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['imagen'] = instance.imagen.url
        return representation