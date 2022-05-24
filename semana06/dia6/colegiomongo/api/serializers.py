#from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer

from .models import Matricula

class MatriculaSerializer(DocumentSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'
        extra_kwargs = {'id':{'read_only':True}}