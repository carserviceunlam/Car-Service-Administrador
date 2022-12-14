# Generated by Django 3.2.13 on 2022-10-24 22:51

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0010_auto_20221019_2107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modules',
            options={'ordering': [django.db.models.expressions.OrderBy(django.db.models.expressions.F('title'), nulls_last=True)]},
        ),
        migrations.AddConstraint(
            model_name='customer_modules',
            constraint=models.UniqueConstraint(fields=('module_segmentacion_id', 'customer_id'), name='name of constraint'),
        ),
    ]
