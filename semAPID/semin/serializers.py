from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class PacienteSerializer(serializers.ModelSerializer):  
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Paciente
        fields = "__all__"


class ExpedienteSerializer(serializers.ModelSerializer):  

    class Meta:
        model = Expediente
        fields = "__all__"



class UserSerializer(serializers.ModelSerializer):  
    paciente = serializers.PrimaryKeyRelatedField(many=True, queryset=Paciente.objects.all())

    class Meta:
        model = User
        fields = "__all__"
#        fields = ('id', 'username', 'email', 'id_sem', 'tipo', 'titulo')

