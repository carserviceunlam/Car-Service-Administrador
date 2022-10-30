from operator import truediv
from django.db import models
from apps.ubicacion.models import Ciudad
from apps.personas.models import Persona
from django.contrib.auth.models import User
# Create your models here.


class Cliente(models.Model):
    cuit_cuil = models.CharField(unique=True,max_length=11,null=False)
    business_name = models.CharField(max_length=128,unique=True)
    phone = models.CharField(null=True,max_length=12)
    mobile = models.CharField(null=True,max_length=10)
    city_id = models.ForeignKey(Ciudad, models.DO_NOTHING)
    address = models.CharField(max_length=254)
    height = models.PositiveIntegerField(default=0)
    email = models.EmailField(blank=True)
    details = models.CharField(max_length=254)
    bank_account_id = models.CharField(max_length=254)
    persons_id = models.ForeignKey(Persona, models.DO_NOTHING)
    state = models.BooleanField(null=False)
    
    def __str__(self):
        return self.business_name

    class Meta:
        
        db_table = 'service_customer'    
    
class cliente_user(models.Model):
    customer_id = models.ForeignKey(Cliente, models.DO_NOTHING)
    user_id = models.ForeignKey(User, models.DO_NOTHING)
    

    class Meta:       
        db_table = 'service_customer_user'