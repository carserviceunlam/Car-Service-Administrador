from django.db import models

# Create your models here.


class Provincia(models.Model):
    name = models.CharField(max_length=128,null=False)
    
    def __str__(self) -> str:
        return "{}".format(self.name)
    class Meta:
        ordering = ["name"]
        db_table = 'service_provinces'
    
class Ciudad(models.Model):
    name = models.CharField(max_length=32)
    province_id = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        db_table = 'service_cities' 