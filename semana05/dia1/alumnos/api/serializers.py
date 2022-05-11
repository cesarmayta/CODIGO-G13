from rest_framework import serializers

from .models import Alumno,Profesor

class AlumnoSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    email = serializers.EmailField()

    def create(self,validated_data):
        return Alumno.objects.create(**validated_data)

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'