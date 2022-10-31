from django import forms


from .models import Cliente


class registerForm(forms.ModelForm):
    cuit_cuil = forms.CharField(min_length=11, max_length=11)
    mobile = forms.CharField(min_length=10, max_length=10)
    phone = forms.CharField(min_length=8, max_length=12)
    class Meta:
        model = Cliente

        fields = {
            'cuit_cuil',
            'business_name',
            'phone',
            'mobile',
            'address',
            'height',
            'email',
            'details',
            'bank_account_id',
            'state',
            'city_id',
            'persons_id'

        }
        
        widgets = {
           
            'business_name': forms.TextInput(attrs={'PlaceHolder': 'business_name'}),          
        }

        labels = {
        'cuit_cuil': 'DNI/CUIT',
        'business_name':'Razon Social',
        'phone':'Telefono',
        'mobile':'Celular',
        'email':'Email',
        'address':'Dirección',
        'height':'Altura',
        'details':'Detalles',
        'bank_account_id':'Cuenta Bancaria',
        'state':'Activo',
        'city_id':'ciudad',
        }
        
