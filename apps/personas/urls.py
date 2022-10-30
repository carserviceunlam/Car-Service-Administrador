from django.urls import path, include
from apps.personas.views import registrarUsuarioCliente, editarUsuarioCliente, registrarPersona, editarPersonas
from apps.personas import views

urlpatterns = [
    path('altaPersona/', registrarPersona.as_view(),name="registrar_persona"),
    path('editarPersona/<int:pk>', editarPersonas.as_view(), name="editar_personas"),
    path('buscarClientes/', views.buscarPersonas),
    path('registrarUsuarioCliente/', registrarUsuarioCliente.as_view(),name="registrar_Usuario_Cliente"),
    path('editarUsuarioCliente/<int:pk>', editarUsuarioCliente.as_view(),name="editar_Usuario_Cliente"),
]
