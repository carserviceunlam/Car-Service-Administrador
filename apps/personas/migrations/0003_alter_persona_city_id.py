# Generated by Django 3.2.13 on 2022-09-27 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ubicacion', '0002_alter_ciudad_province_id'),
        ('personas', '0002_alter_persona_city_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='city_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubicacion.ciudad'),
        ),
    ]
