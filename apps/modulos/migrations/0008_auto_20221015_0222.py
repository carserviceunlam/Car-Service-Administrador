# Generated by Django 3.2.13 on 2022-10-15 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0007_auto_20221015_0056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module_segmentacion',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='modules',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelTable(
            name='customer_modules',
            table='customer_modules',
        ),
        migrations.AlterModelTable(
            name='module_segmentacion',
            table='module_segmentation',
        ),
        migrations.AlterModelTable(
            name='modules',
            table='modules',
        ),
    ]
