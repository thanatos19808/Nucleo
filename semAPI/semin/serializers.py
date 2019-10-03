from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class PacienteSerializer(serializers.ModelSerializer):  

    class Meta:
        model = Paciente
        fields = ('id','nombre','apellido_paterno','apellido_materno','sexo','fecha_nacimiento','tipo_sangre','curp','entidad_nacimiento','entidad','nivel_socioeconomico','tipo_vivienda','discapacidad','grupoEtnico','religion','ocupacion','tipoDomicilio','calle','colonia','num_interior','num_exterior','cp','municipio','localidad','estado','telefonoCasa','telefonoOficina','telefonoCelular','email','fecha_registro')


class ExpedienteSerializer(serializers.ModelSerializer):  

    class Meta:
        model = Expediente
        fields = "__all__"


class HorarioSucursalSerializer(serializers.ModelSerializer):

    class Meta:
        model = HorarioSucursal
        fields = "__all__"


class EstudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estudio
        fields = "__all__"


class SucursalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sucursal
        fields = "__all__"


class DisponibilidadServicioSerializer(serializers.ModelSerializer):

    class Meta:
        model = DisponibilidadServicio
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):  
    paciente = serializers.PrimaryKeyRelatedField(many=True, queryset=Paciente.objects.all())

    class Meta:
        model = User
        fields = "__all__"
#        fields = ('id', 'username', 'email', 'id_sem', 'tipo', 'titulo')

