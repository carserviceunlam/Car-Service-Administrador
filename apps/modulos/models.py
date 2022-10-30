from django.core.exceptions import ValidationError
from django.db import models
from apps.clientes.models import Cliente
from django.db.models import F
from django.contrib.auth.models import Permission


class modules(models.Model):
    title = models.CharField(max_length=40,null=False,unique=True)
    codigo= models.CharField(max_length=40,null=False,unique=True)
    state = models.BooleanField(null=False)
    def __str__(self):
        return self.title
    def clean(self):
        print("desde web")
        print(self.codigo)
        checkCodigo = Permission.objects.filter(codename=self.codigo).first()
        print("print modulo")
        print(checkCodigo)
        if checkCodigo == None:
           raise ValidationError('ingrese un codigo de permiso valido en "codigo modulo"')
        
    class Meta:
        ordering = [F('title').asc(nulls_last=True)]
        db_table = 'service_modules'

class module_segmentacion(models.Model):
     name = models.CharField(max_length=30,null=False,unique=True)
     cost  = models.DecimalField(max_digits=20, decimal_places=2, null=False)
     module_id = models.ManyToManyField(modules)
     state = models.BooleanField(null=False)
     def __str__(self):
        return self.name

     class Meta:
        ordering = ["name"]
        db_table = 'service_module_segmentation'
    
class customer_modules(models.Model):
    module_segmentacion_id = models.ForeignKey(module_segmentacion, models.DO_NOTHING)
    customer_id = models.ForeignKey(Cliente, models.DO_NOTHING)
    highdata =models.DateField(null=True)
    lowdata= models.DateField(null=True)
    state = models.BooleanField(null=True)
      
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['module_segmentacion_id', 'customer_id'], name='name of constraint')
        ]
        db_table = 'service_customer_modules'

