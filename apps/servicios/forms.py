from dataclasses import field
from django import forms
from .models import BD, Website


class formBD(forms.ModelForm):
    
    class Meta:
        model = BD
        
        fields = {
            'name_bd',
            'user_bd',
            'password_bd',
            'currentSize',
            'TotalSize',
            'customer_id'
        }

class formWebsite(forms.ModelForm):
    
    class Meta:
        model = Website
        
        fields = {
            'name',
            'dns1',
            'dns2',
            'customer_id',
            'plantilla',
            'parrafo_1',
            'parrafo_2',
            'parrafo_3'
        }
        
       