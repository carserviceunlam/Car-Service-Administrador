from dataclasses import field
from django import forms
from .models import Persona
from apps.ubicacion.models import Ciudad
from django.forms.models import ModelMultipleChoiceField
import datetime
class MyMultipleModelChoiceField(ModelMultipleChoiceField):

    def label_from_instance(self, obj):
        return "%s" % (obj.name)

class registroFormPersona(forms.ModelForm):
    dni = forms.CharField(min_length=11, max_length=11)
    mobile = forms.CharField(min_length=10, max_length=10)
    phone = forms.CharField(min_length=8, max_length=12)
    class Meta:
        model = Persona
        
        fields = {
            'dni',
            'name',
            'last_name',
            'birthday',
            'phone',
            'mobile',
            'email',
            'city_id',
            'address',
            'address_number',
            'created_date'
        }
        
        widgets = {
            'dni': forms.TextInput(attrs={'PlaceHolder': 'cuit-cuil'}),
            'name': forms.TextInput(attrs={'placeHolder': 'nombre cliente'}),
            'last_name': forms.TextInput(attrs={'placeHolder': 'apellido cliente'}),
            'phone': forms.TextInput(attrs={'placeHolder': 'telefono'}),
            'mobile': forms.TextInput(attrs={'placeHolder': 'celular'}),
            'email': forms.TextInput(attrs={'placeHolder': 'email'}),
            'address': forms.TextInput(attrs={'placeHolder': 'direccion'}),
            'address_number': forms.TextInput(attrs={'placeHolder': 'altura'}),
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            
        }

    
        labels = {
        'dni': 'DNI/CUIT',
        'name':'Nombre',
        'last_name':'Apellido',
        'phone':'Telefono',
        'mobile':'Celular',
        'email':'Email',
        'address':'Dirección',
        'address_number':'Altura',
        'birthday':'Fecha de Nacimiento',
        'city_id':'Ciudad'
        }
