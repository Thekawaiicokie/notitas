# Generated by Django 4.1 on 2022-11-21 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vehiculos", "0002_alter_detallemantencion_vehiculo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="detallemantencion",
            name="precio",
        ),
        migrations.AlterField(
            model_name="detallemantencion",
            name="kilometraje",
            field=models.PositiveIntegerField(),
        ),
    ]
