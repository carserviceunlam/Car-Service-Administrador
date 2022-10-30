from django.urls import path, include
from apps.ubicacion import views

urlpatterns = [
   
  path('ciudad/<int:id>', views.get_ciudad  , name='get_ciudad')

]
