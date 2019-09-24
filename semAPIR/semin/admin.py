from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
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


admin.site.site_header = 'PANEL DE CONTROL SEMIN SERVER'
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Paciente, PacienteAdmin)


