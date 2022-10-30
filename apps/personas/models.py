from apps.ubicacion.models import Ciudad
from django.db import models


# Create your models here.


class Persona(models.Model):
    dni = models.CharField(unique=True,max_length=11,null=False)
    name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday = models.DateField(null=True)
    phone = models.CharField(null=True,max_length=12)
    mobile = models.CharField(null=True,max_length=10)
    email = models.EmailField(unique=True,null=False)
    city_id = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    address = models.CharField(max_length=254)
    address_number = models.PositiveIntegerField(null=True)
    created_date = models.DateField(null=True)
    last_modified_date = models.DateField(null=True)

    
    class Meta:
        ordering = ["dni"]
        db_table = 'service_persons' 