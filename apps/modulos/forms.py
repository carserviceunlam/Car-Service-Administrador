from dataclasses import field
from django import forms
from .models import modules, module_segmentacion, customer_modules

from django.forms.models import ModelMultipleChoiceField,ModelChoiceField


class MyMultipleModelChoiceField(ModelMultipleChoiceField):

    def label_from_instance(self, obj):
        return "%s" % (obj.title)





class registroModulo(forms.ModelForm):

    class Meta:
        model = modules

        fields = {
            'title',
            'state',
            'codigo'
        }

        labels = {
            'title': 'Titulo del modulo',
            'state': 'Activo',
            'codigo': 'Codigo Modulo',

        }

        
class registroSegmentacion(forms.ModelForm):
    

    class Meta:
        model = module_segmentacion

        
        fields = {
            'name',
            'cost',
            'module_id',
            'state'
        }
        labels = {
            'name': 'Nombre del Plan',
            'cost': 'Costo',
            'module_id': 'Modulos disponibles'
        }
    def __init__(self, *args, **kwargs):

        # call the parent init
         super(registroSegmentacion, self).__init__(*args, **kwargs)

         self.fields['module_id'] = MyMultipleModelChoiceField(
            queryset=modules.objects.filter(state=1), 
            required=True, 
            widget=forms.SelectMultiple())

    

class asignarModulos(forms.ModelForm):

    class Meta:
        model = customer_modules

        fields = {
            'module_segmentacion_id',
            'customer_id',
        }
        labels = {
            'module_segmentacion_id': 'Planes disponibles',
            'customer_id': 'Empresa',
        }
        
    def __init__(self, *args, **kwargs):

        # call the parent init
         super(asignarModulos, self).__init__(*args, **kwargs)

         self.fields['module_segmentacion_id'] = ModelChoiceField(
            queryset=module_segmentacion.objects.filter(state=1), 
            required=True, 
            widget=forms.Select())