# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from apps.modulos.views import registrarModulo,editarModulo, asignarModulos,registrarPlan, editarPlan, buscarPlanes, retirarModulos
from apps.modulos import views

urlpatterns = [

    path('alta/modulo/', registrarModulo.as_view() , name="register_modulo"),
    path('editar/modulo/<int:pk>', editarModulo.as_view(),name="editar_modulo"),
    path('buscar/modulos/', views.buscarModulos),
    path('asignarModulos/', asignarModulos.as_view(),name="asignar_modulos"),
    path('alta/plan/', registrarPlan.as_view(),name="alta_plan"),
    path('editar/Plan/<int:pk>', editarPlan.as_view(),name="editar_plan"),
    path('buscar/planes/', buscarPlanes.as_view() ,name="editar_plan"),
     path('retirar/plan/<id>', views.retirarModulos,name="retirar_modulos"),
]
 