# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from apps.authentication.views import registrarUsuarioSistema , buscarUsuarios, editarUsuarioSistema

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('register/usuario/', registrarUsuarioSistema.as_view() , name="register_usuario_sistema"),
    path('editar/usuario/<int:pk>', editarUsuarioSistema.as_view(),name="editar_usuario_sistema"),
    path("buscar/usuarios/", buscarUsuarios.as_view(), name="buscar_usuarios"),
    path("logout/", LogoutView.as_view(), name="logout")
]
