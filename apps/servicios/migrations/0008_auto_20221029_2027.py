# Generated by Django 3.2.13 on 2022-10-29 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0007_alter_website_name'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='bd',
            table='service_customerBD',
        ),
        migrations.AlterModelTable(
            name='website',
            table='service_website',
        ),
    ]