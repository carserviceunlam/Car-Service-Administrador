from django.contrib import admin

from .models import Provincia
from .models import Ciudad
# Register your models here.
admin.site.register(Provincia)
admin.site.register(Ciudad)
