# Generated by Django 3.2.13 on 2022-10-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0009_alter_persona_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='mobile',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='phone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]