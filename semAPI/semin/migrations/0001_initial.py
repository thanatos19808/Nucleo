# Generated by Django 2.2.5 on 2019-09-25 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=200, null=True)),
                ('prueba', models.CharField(max_length=200, null=True)),
                ('sinAcro', models.CharField(max_length=200, null=True)),
                ('beneficio', models.CharField(max_length=200, null=True)),
                ('tipoMuestra', models.CharField(max_length=100, null=True)),
                ('indicacionesPreExamen', models.CharField(max_length=1000, null=True)),
                ('tiempoEntrega', models.CharField(max_length=45, null=True)),
                ('precioVenta', models.FloatField(null=True)),
                ('DIFPue', models.FloatField(null=True)),
                ('ISSSTEPAtlixco', models.FloatField(null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('ultimaActualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Semin - Catálogo de Estudios',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=90, null=True)),
                ('puesto', models.CharField(max_length=90, null=True)),
                ('apellido_paterno', models.CharField(max_length=45, null=True)),
                ('apellido_materno', models.CharField(blank=True, max_length=45, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('masculino', 'masculino'), ('femenino', 'femenino')], max_length=9, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=45, null=True, unique=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('ultimaActualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Semin - Empleados',
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreSucursal', models.CharField(blank=True, max_length=90, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('calle', models.CharField(blank=True, max_length=90, null=True)),
                ('colonia', models.CharField(blank=True, max_length=45, null=True)),
                ('num_interior', models.CharField(blank=True, max_length=10, null=True)),
                ('num_exterior', models.CharField(blank=True, max_length=10, null=True)),
                ('cp', models.CharField(blank=True, max_length=5, null=True)),
                ('municipio', models.CharField(blank=True, max_length=45, null=True)),
                ('localidad', models.CharField(blank=True, max_length=200, null=True)),
                ('estado', models.CharField(blank=True, choices=[('Aguascalientes', 'Aguascalientes'), ('Baja California', 'Baja California'), ('Baja California Sur', 'Baja California Sur'), ('Campeche', 'Campeche'), ('CDMX', 'CDMX'), ('Chihuahua', 'Chihuahua'), ('Chiapas', 'Chiapas'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('México', 'México'), ('Michoacán', 'Michoacán'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo León', 'Nuevo León'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Querétaro', 'Querétaro'), ('Quintana Ro', 'Quintana Ro'), ('San Luis Potosí', 'San Luis Potosí'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatán', 'Yucatán'), ('Zacatecas', 'Zacatecas')], max_length=20, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('ultimaActualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Semin - Sucursales',
            },
        ),
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, null=True)),
                ('descripcion', models.CharField(max_length=1000, null=True)),
                ('precioVenta', models.FloatField(null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('ultimaActualizacion', models.DateTimeField(auto_now=True)),
                ('Catalogo', models.ManyToManyField(blank=True, to='semin.Catalogo')),
            ],
            options={
                'verbose_name_plural': 'Semin - Catálogo de Estudios - Promociones',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_sem', models.IntegerField(blank=True, null=True)),
                ('tipo', models.CharField(blank=True, choices=[('Doctor', 'Doctor'), ('Paciente', 'Paciente'), ('Laboratorio', 'Laboratorio')], max_length=9, null=True)),
                ('titulo', models.CharField(blank=True, choices=[('Dr.', 'Dr.'), ('Dra.', 'Dra.')], max_length=4, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=90, null=True)),
                ('apellido_paterno', models.CharField(max_length=45, null=True)),
                ('apellido_materno', models.CharField(blank=True, max_length=45, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('masculino', 'masculino'), ('femenino', 'femenino')], max_length=9, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('tipo_sangre', models.CharField(blank=True, choices=[('N/A', 'No Definida'), ('A+', 'A Positiva'), ('A-', 'A Negativo'), ('B+', 'B Positivo'), ('B-', 'B Negativo'), ('O+', 'O Positivo'), ('O-', 'O Negativo'), ('AB+', 'AB Positivo'), ('AB-', 'AB Negativo')], max_length=3, null=True)),
                ('curp', models.CharField(blank=True, max_length=18, null=True, unique=True)),
                ('entidad_nacimiento', models.CharField(blank=True, choices=[('Aguascalientes', 'Aguascalientes'), ('Baja California', 'Baja California'), ('Baja California Sur', 'Baja California Sur'), ('Campeche', 'Campeche'), ('CDMX', 'CDMX'), ('Chihuahua', 'Chihuahua'), ('Chiapas', 'Chiapas'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('México', 'México'), ('Michoacán', 'Michoacán'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo León', 'Nuevo León'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Querétaro', 'Querétaro'), ('Quintana Ro', 'Quintana Ro'), ('San Luis Potosí', 'San Luis Potosí'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatán', 'Yucatán'), ('Zacatecas', 'Zacatecas')], max_length=20, null=True)),
                ('entidad', models.CharField(blank=True, choices=[('Aguascalientes', 'Aguascalientes'), ('Baja California', 'Baja California'), ('Baja California Sur', 'Baja California Sur'), ('Campeche', 'Campeche'), ('CDMX', 'CDMX'), ('Chihuahua', 'Chihuahua'), ('Chiapas', 'Chiapas'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('México', 'México'), ('Michoacán', 'Michoacán'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo León', 'Nuevo León'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Querétaro', 'Querétaro'), ('Quintana Ro', 'Quintana Ro'), ('San Luis Potosí', 'San Luis Potosí'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatán', 'Yucatán'), ('Zacatecas', 'Zacatecas')], max_length=20, null=True)),
                ('nivel_socioeconomico', models.CharField(blank=True, max_length=90, null=True)),
                ('tipo_vivienda', models.CharField(blank=True, max_length=90, null=True)),
                ('discapacidad', models.CharField(blank=True, max_length=90, null=True)),
                ('grupoEtnico', models.CharField(blank=True, max_length=90, null=True)),
                ('religion', models.CharField(blank=True, max_length=45, null=True)),
                ('ocupacion', models.CharField(blank=True, max_length=90, null=True)),
                ('tipoDomicilio', models.CharField(blank=True, max_length=90, null=True)),
                ('calle', models.CharField(blank=True, max_length=90, null=True)),
                ('colonia', models.CharField(blank=True, max_length=45, null=True)),
                ('num_interior', models.CharField(blank=True, max_length=10, null=True)),
                ('num_exterior', models.CharField(blank=True, max_length=10, null=True)),
                ('cp', models.CharField(blank=True, max_length=5, null=True)),
                ('municipio', models.CharField(blank=True, max_length=45, null=True)),
                ('localidad', models.CharField(blank=True, max_length=200, null=True)),
                ('estado', models.CharField(blank=True, choices=[('Aguascalientes', 'Aguascalientes'), ('Baja California', 'Baja California'), ('Baja California Sur', 'Baja California Sur'), ('Campeche', 'Campeche'), ('CDMX', 'CDMX'), ('Chihuahua', 'Chihuahua'), ('Chiapas', 'Chiapas'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('México', 'México'), ('Michoacán', 'Michoacán'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo León', 'Nuevo León'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Querétaro', 'Querétaro'), ('Quintana Ro', 'Quintana Ro'), ('San Luis Potosí', 'San Luis Potosí'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatán', 'Yucatán'), ('Zacatecas', 'Zacatecas')], max_length=20, null=True)),
                ('telefonoCasa', models.IntegerField(blank=True, null=True)),
                ('telefonoOficina', models.IntegerField(blank=True, null=True)),
                ('telefonoCelular', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=45, null=True, unique=True)),
                ('fecha_registro', models.DateField(blank=True, null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('ultimaActualizacion', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semin', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='HorarioSucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('1', 'Lun'), ('2', 'Mar'), ('3', 'Mie'), ('4', 'Jue'), ('5', 'Vie'), ('6', 'Sab'), ('7', 'Dom')], max_length=1, null=True)),
                ('hora_inicio', models.TimeField(null=True)),
                ('hora_final', models.TimeField(null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('ultimaActualizacion', models.DateTimeField(auto_now=True)),
                ('Sucursal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='semin.Sucursal')),
            ],
            options={
                'verbose_name_plural': 'Semin - Sucursales',
            },
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numExpediente', models.CharField(blank=True, max_length=90, null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('ultimaActualizacion', models.DateTimeField(auto_now=True)),
                ('Paciente', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='semin.Paciente')),
            ],
            options={
                'verbose_name_plural': 'Pacientes - Expedientes',
            },
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaEstudio', models.DateField(blank=True, null=True)),
                ('tipoEstudio', models.CharField(blank=True, max_length=90, null=True)),
                ('urlEstudio', models.CharField(blank=True, max_length=200, null=True)),
                ('notasEstudio', models.CharField(blank=True, max_length=500, null=True)),
                ('Expediente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='semin.Expediente')),
            ],
            options={
                'verbose_name_plural': 'Pacientes - Estudios',
            },
        ),
        migrations.CreateModel(
            name='DisponibilidadServicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tomaMuestras', models.BooleanField(blank=True, default=False, null=True)),
                ('ultrasonografia', models.BooleanField(blank=True, default=False, null=True)),
                ('rayosX', models.BooleanField(blank=True, default=False, null=True)),
                ('rayosXContrastados', models.BooleanField(blank=True, default=False, null=True)),
                ('mastografia', models.BooleanField(blank=True, default=False, null=True)),
                ('patologia', models.BooleanField(blank=True, default=False, null=True)),
                ('electrocardiograma', models.BooleanField(blank=True, default=False, null=True)),
                ('tomografia', models.BooleanField(blank=True, default=False, null=True)),
                ('resonanciaMagnetica', models.BooleanField(blank=True, default=False, null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('ultimaActualizacion', models.DateTimeField(auto_now=True)),
                ('Sucursal', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='semin.Sucursal')),
            ],
            options={
                'verbose_name_plural': 'Semin - Sucursales - Disponibilidad de Servicios',
            },
        ),
        migrations.CreateModel(
            name='CitaSucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateField(null=True)),
                ('titulo', models.CharField(max_length=45, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=1000, null=True)),
                ('notas', models.CharField(max_length=200, null=True)),
                ('estatus', models.CharField(blank=True, choices=[('ACTIVA', 'ACTIVA'), ('CERRADA', 'CERRADA'), ('CANCELADA', 'CANCELADA'), ('ESPERA', 'ESPERA')], max_length=13, null=True)),
                ('hora_inicio', models.TimeField(null=True)),
                ('hora_final', models.TimeField(null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('ultimaActualizacion', models.DateTimeField(auto_now=True)),
                ('Sucursal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='semin.Sucursal')),
            ],
            options={
                'verbose_name_plural': 'Semin - Sucursales - Citas',
            },
        ),
        migrations.AddField(
            model_name='catalogo',
            name='CitaSucrusal',
            field=models.ManyToManyField(blank=True, to='semin.CitaSucursal'),
        ),
    ]
