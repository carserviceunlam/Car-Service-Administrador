from venv import create
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import Permission
from apps.clientes.models import Cliente, cliente_user
from .models import Persona
from django.core import serializers
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from .forms import registroFormPersona
from apps.authentication.forms import SignUpForm,  editUpForm
from django.contrib import messages
from apps.ubicacion.models import Ciudad
from apps.modulos.models import customer_modules
from django.urls import reverse_lazy
from datetime import date
from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.mixins import LoginRequiredMixin
import MySQLdb
import json
# Create your views here.



class registrarPersona(LoginRequiredMixin,CreateView):
    model = Persona
    form_class = registroFormPersona
    template_name = "persona/altaPersona.html"
    
    def post(self, request, *args, **Kwargs):

        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                persona = form.save()
                messages.success(request, 'ok')
                return redirect('/editarPersona/' + str(persona.id), args={request})
            else:
                return render(
                    request=request,
                    template_name=self.template_name,
                    context={"form": form},
                )

   
class editarPersonas(LoginRequiredMixin,UpdateView):
    model = Persona
    form_class = registroFormPersona
    template_name = "persona/editarClientes.html"

    def get_context_data(self, **kwargs):
       
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        cliente =Cliente.objects.filter(persons_id= self.kwargs['pk'])
        context['cliente'] = cliente
        context['customerModules'] = customer_modules.objects.all()
        context['clienteJson'] = serializers.serialize("json", cliente)
        return context
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'se gurdaron los cambios!')
        return reverse_lazy('editar_personas', args=[self.get_object().pk])




@login_required(login_url="/login/")
def buscarPersonas(request):

    persona = Persona.objects.all()
    return render(request, "home/buscarClientes.html", {"persona": persona})


def enviarEmail(data,usuario,contraseña):
    context = {'mail': data,'usuario':usuario,'contraseña':contraseña}
    template = get_template('email/email.html')
    content = template.render(context)
    email = EmailMultiAlternatives(
        'Bienvenido',
        'Car Service',
        settings.EMAIL_HOST_USER,
        [data]

    )
    email.attach_alternative(content, 'text/html')
    email.send()


class registrarUsuarioCliente(LoginRequiredMixin, CreateView):

    model = User
    form_class = SignUpForm
    template_name = "usuario_cliente/alta_usuario.html"

    def post(self, request, *args, **Kwargs):

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                user = form.save()
                email = form.cleaned_data.get('email')
                nombreUsuario=form.cleaned_data.get('username')
                contraseña=request.POST['password1']
                enviarEmail(email,nombreUsuario,contraseña,)
                customer = Cliente.objects.get(id=request.POST['customerID'])
                cliente_user.objects.create(customer_id=customer, user_id=user)
                plan = customer_modules.objects.filter(
                    customer_id=request.POST['customerID'])
                for p in plan:
                    print(p.module_segmentacion_id.module_id.all())
                    for m in p.module_segmentacion_id.module_id.all():
                        print(m.codigo)
                        permission = Permission.objects.get(codename=m.codigo)
                        user.user_permissions.add(permission)

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


class editarUsuarioCliente(LoginRequiredMixin, UpdateView):

    model = User
    form_class = editUpForm
    template_name = "usuario_cliente/editar_usuario.html"

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
