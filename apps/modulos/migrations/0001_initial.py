# Generated by Django 3.2.13 on 2022-10-11 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0004_alter_cliente_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('state', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='module_segmentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=20)),
                ('module_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulos.modules')),
            ],
        ),
        migrations.CreateModel(
            name='customer_modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highdata', models.DateField(null=True)),
                ('lowdata', models.DateField(null=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clientes.cliente')),
                ('module_segmentacion_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modulos.module_segmentacion')),
            ],
        ),
    ]
