# Generated by Django 3.2.13 on 2022-10-20 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0009_alter_module_segmentacion_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modules',
            options={},
        ),
        migrations.AlterField(
            model_name='module_segmentacion',
            name='state',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]