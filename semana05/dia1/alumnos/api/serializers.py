from rest_framework import serializers

class AlumnoSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    email = serializers.EmailField()