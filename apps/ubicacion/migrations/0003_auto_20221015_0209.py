# Generated by Django 3.2.13 on 2022-10-15 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ubicacion', '0002_alter_ciudad_province_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='provincia',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelTable(
            name='ciudad',
            table='cities',
        ),
        migrations.AlterModelTable(
            name='provincia',
            table='provinces',
        ),
    ]
