# Generated by Django 3.2.13 on 2022-10-29 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0007_alter_persona_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='dni',
            field=models.CharField(max_length=11),
        ),
    ]
