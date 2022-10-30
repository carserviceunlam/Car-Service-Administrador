# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    # Auth routes - login / register
    path("", include("apps.authentication.urls")),

    # ADD NEW Routes HERE

    # Leave `Home.Urls` as last the last line
    path("", include("apps.ubicacion.urls")),
    path("", include("apps.servicios.urls")),
    path("", include("apps.clientes.urls")),
    path("", include("apps.personas.urls")),
    path("", include("apps.modulos.urls")),
    path("", include("apps.home.urls")),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
