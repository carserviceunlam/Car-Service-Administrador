# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from apps.clientes.views import registrarCliente
urlpatterns = [

    # The home page
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('customer/<slug:slug>', views.custom, name='customers'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
