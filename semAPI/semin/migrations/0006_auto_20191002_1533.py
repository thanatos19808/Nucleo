# Generated by Django 2.2.5 on 2019-10-02 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semin', '0005_auto_20190925_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='nombreSucursal',
            field=models.CharField(max_length=90, null=True),
        ),
    ]
