from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError

USER_TYPE_CHOICES = (
    ('Doctor', 'Doctor'),
    ('Paciente','Paciente'),
    ('Laboratorio','Laboratorio'),
)

SEX_CHOICES = (
    ('masculino', 'masculino'),
    ('femenino','femenino'),
)

BLOOD_CHOICES = (
    ('N/A', 'No Definida'),
    ('A+', 'A Positiva'),
    ('A-', 'A Negativo'),
    ('B+', 'B Positivo'),
    ('B-', 'B Negativo'),
    ('O+', 'O Positivo'),
    ('O-', 'O Negativo'),
    ('AB+', 'AB Positivo'),
    ('AB-', 'AB Negativo'),
)

STATUS_CHOICES = (
    ('Activa', 'Activa'),
    ('Desactivada','Desactivada'),
    ('Des_pago','Desactivada_Pago'),
    ('Des_eliminada','Desactivada_Eliminada'),
    ('Des_inactiva','Desactivada_Inactiva'),
)

APPOINTMENT_STATUS_CHOICES = (
('ACTIVA','ACTIVA'),
('CERRADA','CERRADA'),
('CANCELADA','CANCELADA'),
('ESPERA','ESPERA'),
)

TITLE_CHOICES = (
    ('Dr.', 'Dr.'),
    ('Dra.','Dra.'),
)

STATE_CHOICES = (
    ('Aguascalientes','Aguascalientes'),
    ('Baja California','Baja California'),
    ('Baja California Sur','Baja California Sur'),
    ('Campeche','Campeche'),
    ('CDMX','CDMX'),
    ('Chihuahua','Chihuahua'),
    ('Chiapas','Chiapas'),
    ('Coahuila','Coahuila'),    
    ('Colima','Colima'),
    ('Durango','Durango'),
    ('Guanajuato','Guanajuato'),
    ('Guerrero','Guerrero'),
    ('Hidalgo','Hidalgo'),
    ('Jalisco','Jalisco'),
    ('México','México'),
    ('Michoacán','Michoacán'),
    ('Morelos','Morelos'),
    ('Nayarit','Nayarit'),
    ('Nuevo León','Nuevo León'),
    ('Oaxaca','Oaxaca'),
    ('Puebla','Puebla'),
    ('Querétaro','Querétaro'),
    ('Quintana Ro','Quintana Ro'),
    ('San Luis Potosí','San Luis Potosí'),
    ('Sinaloa','Sinaloa'),
    ('Sonora','Sonora'),
    ('Tabasco','Tabasco'),
    ('Tamaulipas','Tamaulipas'),
    ('Tlaxcala','Tlaxcala'),
    ('Veracruz','Veracruz'),
    ('Yucatán','Yucatán'),
    ('Zacatecas','Zacatecas'),
)

DAY_CHOICES = (
    ('1', 'Lun'),
    ('2', 'Mar'),
    ('3', 'Mie'),
    ('4', 'Jue'),
    ('5', 'Vie'),
    ('6', 'Sab'),
    ('7', 'Dom'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_sem = models.IntegerField(null=True, blank=True)
    tipo = models.CharField(max_length=9,null=True, blank=True, choices=USER_TYPE_CHOICES)
    titulo = models.CharField(max_length=4,null=True, blank=True, choices=TITLE_CHOICES)

    class Meta:
        verbose_name = _("Perfil")
        verbose_name_plural = _("Perfiles")
        ordering = ("user",)

    def __str__(self):
        return self.user.username
 

class Empleado(models.Model):
    nombre = models.CharField(max_length=90,null=True, blank=False)
    puesto = models.CharField(max_length=90,null=True, blank=False)
    apellido_paterno = models.CharField(max_length=45,null=True, blank=False)
    apellido_materno = models.CharField(max_length=45,null=True, blank=True)
    sexo = models.CharField(max_length=9,null=True, blank=True, choices=SEX_CHOICES)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=45, unique=True ,null=True, blank=True)
    creacion = models.DateTimeField(auto_now_add=True) # When it was create
    ultimaActualizacion = models.DateTimeField(auto_now=True) # When i was update

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.apellido_paterno, self.apellido_materno)

    class Meta:
        verbose_name_plural = "Semin - Empleados"


class Paciente(models.Model):
    nombre = models.CharField(max_length=90,null=True, blank=False)
    apellido_paterno = models.CharField(max_length=45,null=True, blank=False)
    apellido_materno = models.CharField(max_length=45,null=True, blank=True)
    sexo = models.CharField(max_length=9,null=True, blank=True, choices=SEX_CHOICES)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    tipo_sangre = models.CharField(max_length=3,null=True, blank=True, choices=BLOOD_CHOICES)
    curp = models.CharField(max_length=18, unique=True ,null=True, blank=True)
    entidad_nacimiento = models.CharField(max_length=20,null=True, blank=True, choices=STATE_CHOICES)
    entidad = models.CharField(max_length=20,null=True, blank=True, choices=STATE_CHOICES)
    nivel_socioeconomico= models.CharField(max_length=90 ,null=True, blank=True)
    tipo_vivienda= models.CharField(max_length=90 ,null=True, blank=True)
    discapacidad= models.CharField(max_length=90 ,null=True, blank=True)
    grupoEtnico= models.CharField(max_length=90 ,null=True, blank=True)
    religion= models.CharField(max_length=45 ,null=True, blank=True)
    ocupacion= models.CharField(max_length=90 ,null=True, blank=True)
    tipoDomicilio= models.CharField(max_length=90 ,null=True, blank=True)
    calle = models.CharField(max_length=90, null=True, blank=True)
    colonia = models.CharField(max_length=45,null=True, blank=True)
    num_interior = models.CharField(max_length=10,null=True, blank=True)
    num_exterior = models.CharField(max_length=10,null=True, blank=True)
    cp = models.CharField(max_length=5,null=True, blank=True)
    municipio = models.CharField(max_length=45,null=True, blank=True)
    localidad = models.CharField(max_length=200,null=True, blank=True)
    estado = models.CharField(max_length=20,null=True, blank=True, choices=STATE_CHOICES)
    telefonoCasa = models.IntegerField(null=True, blank=True)
    telefonoOficina = models.IntegerField(null=True, blank=True)
    telefonoCelular = models.IntegerField(null=True, blank=True) 
    email = models.EmailField(max_length=45, unique=True ,null=True, blank=True)
    fecha_registro = models.DateField(null=True, blank=True)
    creacion = models.DateTimeField(auto_now_add=True) # When it was create
    ultimaActualizacion = models.DateTimeField(auto_now=True) # When i was update
    creator = models.ForeignKey('auth.User', related_name='semin', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.apellido_paterno, self.apellido_materno)

    class Meta:
        verbose_name_plural = "Pacientes"


class Expediente(models.Model):
    numExpediente = models.CharField(max_length=90,null=True, blank=True)
    creacion = models.DateTimeField(auto_now_add=True) # When it was create
    ultimaActualizacion = models.DateTimeField(auto_now=True) # When i was update
    Paciente = models.OneToOneField(Paciente, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s' % (self.numExpediente, self.Paciente.nombre, self.Paciente.apellido_paterno, self.Paciente.apellido_materno)

    class Meta:
        verbose_name_plural = "Pacientes - Expedientes"


class Estudio(models.Model):
    fechaEstudio = models.DateField(null=True, blank=True)
    tipoEstudio = models.CharField(max_length=90, null=True, blank=True)
    urlEstudio = models.CharField(max_length=200, null=True, blank=True)
    notasEstudio = models.CharField(max_length=500, null=True, blank=True)
    Expediente = models.ForeignKey(Expediente, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s %s' % (self.fechaEstudio, self.tipoEstudio, self.Expediente.Paciente.nombre, self.Expediente.Paciente.apellido_paterno, self.Expediente.Paciente.apellido_materno)

    class Meta:
        verbose_name_plural = "Pacientes - Estudios"


class Sucursal(models.Model):
    nombreSucursal = models.CharField(max_length=90,null=True, blank=True)
    descripcion = models.CharField(max_length=200,null=True, blank=True)
    calle = models.CharField(max_length=90, null=True, blank=True)
    colonia = models.CharField(max_length=45,null=True, blank=True)
    num_interior = models.CharField(max_length=10,null=True, blank=True)
    num_exterior = models.CharField(max_length=10,null=True, blank=True)
    cp = models.CharField(max_length=5,null=True, blank=True)
    municipio = models.CharField(max_length=45,null=True, blank=True)
    localidad = models.CharField(max_length=200,null=True, blank=True)
    estado = models.CharField(max_length=20,null=True, blank=True, choices=STATE_CHOICES)
    telefono = models.IntegerField(null=True, blank=True)
    creacion = models.DateTimeField(auto_now_add=True) # When it was create
    ultimaActualizacion = models.DateTimeField(auto_now=True) # When i was update

    def __str__(self):
        return '%s' % (self.nombreSucursal)

    class Meta:
        verbose_name_plural = "Semin - Sucursales"


class DisponibilidadServicios(models.Model):
    tomaMuestras = models.BooleanField(default=False,null=True, blank=True)
    ultrasonografia = models.BooleanField(default=False,null=True, blank=True)
    rayosX = models.BooleanField(default=False,null=True, blank=True)
    rayosXContrastados = models.BooleanField(default=False,null=True, blank=True)
    mastografia = models.BooleanField(default=False,null=True, blank=True)
    patologia = models.BooleanField(default=False,null=True, blank=True)
    electrocardiograma = models.BooleanField(default=False,null=True, blank=True)
    tomografia = models.BooleanField(default=False,null=True, blank=True)
    resonanciaMagnetica = models.BooleanField(default=False,null=True, blank=True)
    creacion = models.DateTimeField(auto_now_add=True) # When it was create
    ultimaActualizacion = models.DateTimeField(auto_now=True) # When i was update
    Sucursal = models.OneToOneField(Sucursal, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s,' % (self.tomaMuestras, self.ultrasonografia, self.rayosX, self.rayosXContrastados, self.mastografia, self.patologia, self.electrocardiograma, self.tomografia, self.resonanciaMagnetica)

    class Meta:
        verbose_name_plural = "Semin - Sucursales - Disponibilidad de Servicios"



class HorarioSucursal(models.Model):
    dia = models.CharField(max_length=1,null=True, blank=False, choices=DAY_CHOICES)
    hora_inicio = models.TimeField(null=True, blank=False)
    hora_final = models.TimeField(null=True, blank=False)
    creacion = models.DateTimeField(auto_now_add=True) # When it was create
    ultimaActualizacion = models.DateTimeField(auto_now=True) # When i was update
    Sucursal = models.ForeignKey(Sucursal, null=True, blank=False, on_delete=models.CASCADE)


    def __str__(self):
        return '%s, %s ,%s ,%s' % (self.dia, self.hora_inicio, self.hora_final, self.Sucursal.nombreSucursal)

    class Meta:
        verbose_name_plural = "Semin - Sucursales - Horario de Sucursal"


class CitaSucursal(models.Model):
    fecha_cita = models.DateField(null=True, blank=False)
    titulo = models.CharField(max_length=45,null=True, blank=False)
    descripcion = models.CharField(max_length=1000,null=True, blank=True)
    notas = models.CharField(max_length=200,null=True, blank=False)
    estatus = models.CharField(max_length=13,null=True, blank=True, choices=APPOINTMENT_STATUS_CHOICES)
    hora_inicio = models.TimeField(null=True, blank=False)
    hora_final = models.TimeField(null=True, blank=False)
    creacion = models.DateTimeField(auto_now_add=True) # When it was create
    ultimaActualizacion = models.DateTimeField(auto_now=True) # When i was update
    Sucursal = models.ForeignKey(Sucursal, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s' % (self.fecha_cita, self.Sucursal.nombreSucursal)

    class Meta:
        verbose_name_plural = "Semin - Sucursales - Citas"


class Catalogo(models.Model):
    area = models.CharField(max_length=200,null=True, blank=False)
    prueba = models.CharField(max_length=200,null=True, blank=False)
    sinAcro = models.CharField(max_length=200,null=True, blank=False)
    beneficio = models.CharField(max_length=200,null=True, blank=False)
    tipoMuestra = models.CharField(max_length=100,null=True, blank=False)
    indicacionesPreExamen = models.CharField(max_length=1000,null=True, blank=False)
    tiempoEntrega = models.CharField(max_length=45,null=True, blank=False)
    precioVenta = models.FloatField(null=True, blank=False)
    DIFPue = models.FloatField(null=True, blank=False)
    ISSSTEPAtlixco = models.FloatField(null=True, blank=False)
    creacion = models.DateTimeField(auto_now_add=True) # When it was create
    ultimaActualizacion = models.DateTimeField(auto_now=True) # When i was update
    CitaSucrusal = models.ManyToManyField(CitaSucursal, blank=True)

    def __str__(self):
        return '%s, %s, %s, %s, %s' % (self.area, self.prueba, self.precioVenta, self.DIFPue, self.ISSSTEPAtlixco)

    class Meta:
        verbose_name_plural = "Semin - Catálogo de Estudios"


class Promocion(models.Model):
    titulo = models.CharField(max_length=200,null=True, blank=False)
    descripcion = models.CharField(max_length=1000,null=True, blank=False)
    precioVenta = models.FloatField(null=True, blank=False)
    creacion = models.DateTimeField(auto_now_add=True) # When it was create
    ultimaActualizacion = models.DateTimeField(auto_now=True) # When i was update
    Catalogo = models.ManyToManyField(Catalogo, blank=True)

    def __str__(self):
        return '%s, %s' % (self.titulo, self.precioVenta)

    class Meta:
        verbose_name_plural = "Semin - Catálogo de Estudios - Promociones"












