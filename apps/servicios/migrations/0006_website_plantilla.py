# Generated by Django 3.2.13 on 2022-10-25 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0005_auto_20221025_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='plantilla',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
