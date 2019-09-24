from rest_framework import serializers
from .models import Paciente
from django.contrib.auth.models import User


class PacienteSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Paciente
        fields = ('title', 'genre', 'year', 'creator')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer usermodel
    paciente = serializers.PrimaryKeyRelatedField(many=True, queryset=Paciente.objects.all())

    class Meta:
        model = User
        fields = "__all__"
#        fields = ('id', 'username', 'email', 'id_sem', 'tipo', 'titulo')

