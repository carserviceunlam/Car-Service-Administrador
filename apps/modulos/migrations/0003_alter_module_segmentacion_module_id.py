# Generated by Django 3.2.13 on 2022-10-11 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0002_alter_modules_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module_segmentacion',
            name='module_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='modulos.modules'),
        ),
    ]
