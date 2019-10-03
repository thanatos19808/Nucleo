from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.db.models.functions import Lower

from .models import *

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

class PacienteAdmin(admin.ModelAdmin):
    class Meta:
        model = Paciente

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ["puesto","nombre","apellido_paterno","apellido_materno"]
    search_fields = ["puesto","nombre","apellido_paterno","apellido_materno"]
    class Meta:
        model = Empleado


class PacienteAdmin(admin.ModelAdmin):
    list_display = ["nombre","apellido_paterno","apellido_materno"]
    search_fields = ["nombre","apellido_paterno","apellido_materno"]
    class Meta:
        model = Paciente


class ExpedienteAdmin(admin.ModelAdmin):
    list_display = ["numExpediente", "paciente__nombre", "paciente__apellido_paterno", "paciente__apellido_materno"]
    search_fields = ["numExpediente", "paciente__nombre", "paciente__apellido_paterno", "paciente__apellido_materno"]

    def paciente__nombre(self, instance):
        return instance.Paciente.nombre

    def paciente__apellido_paterno(self, instance):
        return instance.Paciente.apellido_paterno

    def paciente__apellido_materno(self, instance):
        return instance.Paciente.apellido_materno

    class Meta:
        model = Expediente


class EstudioAdmin(admin.ModelAdmin):
    list_display = ["expediente__numExpediente", "fechaEstudio", "tipoEstudio"]
    search_fields = ["expediente__numExpediente", "fechaEstudio", "tipoEstudio"]

    def expediente__numExpediente(self, instance):
        return instance.Paciente.numExpediente

    class Meta:
        model = Estudio


class SucursalAdmin(admin.ModelAdmin):
    list_display = ["nombreSucursal"]
    search_fields = ["nombreSucursal"]

    class Meta:
        model = Sucursal


class DisponibilidadServicioAdmin(admin.ModelAdmin):
    list_display = ["Nombre__Sucursal", "tomaMuestras", "ultrasonografia", "rayosX", "rayosXContrastados", "mastografia", "patologia", "electrocardiograma", "tomografia", "resonanciaMagnetica"]
    search_fields = ["Nombre__Sucursal", "tomaMuestras", "ultrasonografia", "rayosX", "rayosXContrastados", "mastografia", "patologia", "electrocardiograma", "tomografia", "resonanciaMagnetica"]

#FRONT

    def get_ordering(self, request):
        return [Lower('Sucursal__nombreSucursal')]

    def Nombre__Sucursal(self, instance):
        return instance.Sucursal.nombreSucursal

    class Meta:
        model = DisponibilidadServicio


class HorarioSucursalAdmin(admin.ModelAdmin):
    list_display = ["dia", "hora_inicio", "hora_final", "sucursal__nombreSucursal"]
    search_fields = ["dia", "hora_inicio", "hora_final", "sucursal__nombreSucursal"]

    def sucursal__nombreSucursal(self, instance):
        return instance.Sucursal.nombreSucursal

    class Meta:
        model = HorarioSucursal

class CitaSucursalAdmin(admin.ModelAdmin):
    list_display = ["fecha_cita", "sucursal__nombreSucursal"]
    search_fields = ["fecha_cita", "sucursal__nombreSucursal"]

    def sucursal__nombreSucursal(self, instance):
        return instance.Sucursal.nombreSucursal

    class Meta:
        model = CitaSucursal


class CatalogoAdmin(admin.ModelAdmin):
    list_display = ["area", "prueba", "precioVenta", "DIFPue", "ISSSTEPAtlixco"]
    search_fields = ["area", "prueba", "precioVenta", "DIFPue", "ISSSTEPAtlixco"]

    class Meta:
        model = Catalogo


class PromocionAdmin(admin.ModelAdmin):
    list_display = ["titulo","precioVenta"]
    search_fields = ["titulo","precioVenta"]

    class Meta:
        model = Promocion


admin.site.site_header = 'PANEL DE CONTROL SEMIN SERVER'
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Expediente, ExpedienteAdmin)
admin.site.register(Estudio, EstudioAdmin)
admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(HorarioSucursal, HorarioSucursalAdmin)
admin.site.register(DisponibilidadServicio, DisponibilidadServicioAdmin)
admin.site.register(CitaSucursal, CitaSucursalAdmin)
admin.site.register(Catalogo, CatalogoAdmin)
admin.site.register(Promocion, PromocionAdmin)



