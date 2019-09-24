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
    localidad = models.CharField(max_length=90,null=True, blank=True)
    estado = models.CharField(max_length=20,null=True, blank=True, choices=STATE_CHOICES)
    telefonoCasa = models.IntegerField(null=True, blank=True)
    telefonoOficina = models.IntegerField(null=True, blank=True)
    telefonoCelular = models.IntegerField(null=True, blank=True) 
    email = models.EmailField(max_length=45, unique=True ,null=True, blank=True)
    fecha_registro = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When i was update
    creator = models.ForeignKey('auth.User', related_name='semin', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.apellido_paterno, self.apellido_materno)

    class Meta:
        verbose_name_plural = "Pacientes"

