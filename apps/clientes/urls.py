from django.urls import path, include
from apps.clientes.views import registrarCliente, editarCliente ,eliminarCliente
from apps.clientes import views

urlpatterns = [   
    
    path('registrarCliente/', registrarCliente.as_view(),name="registrar_cliente"),
    path('editarCliente/<int:pk>', editarCliente.as_view(),name="editar_cliente"),
    path('eliminarCliente/<id>', views.eliminarCliente,name="eliminar_cliente"),
    path('cliente/bd/<int:id>', views.get_ciudad_bd  , name='get_ciudad_bd')
    
]
