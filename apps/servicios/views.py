from django.db import connection
from django.shortcuts import render, redirect
from apps.servicios.models import BD, Website
from .forms import formBD, formWebsite
from django.http import JsonResponse
import MySQLdb
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.views.generic import CreateView, UpdateView, View, TemplateView
# Create your views here.


def generarBD(nueva_bd):
    bd = settings.DATABASES['default']['NAME']
    user = settings.DATABASES['default']['USER']
    password = settings.DATABASES['default']['PASSWORD']
    host = settings.DATABASES['default']['HOST']

    query = f'CREATE DATABASE {nueva_bd}; CREATE TABLE {nueva_bd}.admin_website_vehicles LIKE template.admin_website_vehicles;CREATE TABLE {nueva_bd}.admin_website_vehicleowner LIKE template.admin_website_vehicleowner; CREATE TABLE {nueva_bd}.admin_website_repair LIKE template.admin_website_repair;CREATE TABLE {nueva_bd}.admin_website_provinces LIKE template.admin_website_provinces;CREATE TABLE {nueva_bd}.admin_website_providers LIKE template.admin_website_providers;CREATE TABLE {nueva_bd}.admin_website_person LIKE template.admin_website_person;CREATE TABLE {nueva_bd}.admin_website_employee LIKE template.admin_website_employee;CREATE TABLE {nueva_bd}.admin_website_customer LIKE template.admin_website_customer; CREATE TABLE {nueva_bd}.admin_website_companies LIKE template.admin_website_companies;CREATE TABLE {nueva_bd}.admin_website_cities LIKE template.admin_website_cities;INSERT INTO  {nueva_bd}.admin_website_provinces SELECT * FROM template.admin_website_provinces; INSERT INTO  {nueva_bd}.admin_website_cities SELECT * FROM template.admin_website_cities; CREATE TABLE {nueva_bd}.admin_website_budget LIKE template.admin_website_budget;CREATE TABLE {nueva_bd}.admin_website_bankaccounts LIKE template.admin_website_bankaccounts; '
    try:
        db = MySQLdb.connect(
            host=host,
            user=user,
            passwd=password,
            db=bd)
        cur = db.cursor()
        cur.execute(query)
        db.close()

    except MySQLdb.connections.Error as err:
        print("se presento un error: {}".format(err))


class registrarBD(LoginRequiredMixin,CreateView):

    model = BD
    form_class = formBD
    template_name = "bd/alta_bd.html"

    def post(self, request, *args, **Kwargs):

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                generarBD(form.cleaned_data.get('name_bd'))
                mensaje = f'{self.model.__name__} registrado Correctamente'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no sea podido registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            response.status_code = 400
            return response


def get_bd(_request):

    if (BD.objects.last()):
        bd = BD.objects.last()
        query = f"b00{bd.id+1}"
        data = {'message': "Success", 'name_bd': query}
    else:
        data = {'message': "Success", 'name_bd': "b001"}

    return JsonResponse(data)


class registrarWebsite(LoginRequiredMixin,CreateView):

    model = Website
    form_class = formWebsite
    template_name = "website/alta_website.html"

    def post(self, request, *args, **Kwargs):

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                generarBD(form.cleaned_data.get('name_bd'))
                mensaje = f'{self.model.__name__} registrado Correctamente'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no sea podido registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            response.status_code = 400
            return response


class editarWebsite(LoginRequiredMixin,UpdateView):

    model = Website
    form_class = formWebsite
    template_name = "website/editar_website.html"

    def post(self, request, *args, **Kwargs):

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado Correctamente'
                error = 'no hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no sea podido registrar'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return response


class ListadoFacturas(LoginRequiredMixin,TemplateView):

    template_name = "facturacion/listado_facturacion.html"
