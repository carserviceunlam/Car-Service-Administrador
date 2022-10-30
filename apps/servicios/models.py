from tkinter import FALSE
from django.db import models
from apps.clientes.models import Cliente


class BD(models.Model):
    customer_id=models.OneToOneField(Cliente, models.DO_NOTHING)
    name_bd = models.CharField(max_length=30,unique=True,null=True)
    user_bd = models.CharField(max_length=30)
    password_bd = models.CharField(max_length=30)
    currentSize = models.CharField(max_length=30)
    TotalSize = models.CharField(max_length=30)

    class Meta:
        ordering = ["name_bd"]
        db_table = 'service_customerBD'


class Website(models.Model):
    customer_id = models.OneToOneField(Cliente, models.DO_NOTHING)
    name = models.CharField(max_length=30, unique=True)
    parrafo_1 = models.CharField(max_length=30,null=True)
    parrafo_2 = models.CharField(max_length=30,null=True)
    parrafo_3 = models.CharField(max_length=30,null=True)
    plantilla = models.CharField(max_length=30,null=False)
    dns1 = models.CharField(max_length=30)
    dns2 = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        db_table = 'service_website'   
    
    
    