from django.urls import path, include
from apps.servicios import views
from apps.servicios.views import ListadoFacturas, registrarBD, registrarWebsite, editarWebsite

urlpatterns = [
   
    path('registrarBD/', registrarBD.as_view(),name="registrar_bd"),
    path('registrarWebsite/', registrarWebsite.as_view(),name="registrar_bd"),
    path('editarWebsite/<int:pk>',editarWebsite.as_view(),name="editar_website"),
    path('getBD/',views.get_bd,name="get_bd"),
    path('listado/facturas/',ListadoFacturas.as_view(),name="ListadoFacturas"),
]
