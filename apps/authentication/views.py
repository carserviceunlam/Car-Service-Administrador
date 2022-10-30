# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignUpForm ,editUpForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from apps.personas.models import Persona
from django.contrib import messages
from django.views.generic import CreateView, UpdateView ,ListView
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.groups.filter(name='administrador').exists() | user.groups.filter(name='vendedor').exists()|user.is_superuser == 1:
                   login(request, user)
                   return redirect("/")
                else:
                    msg = 'No tiene permisos para ingresar'
            else:
                msg = 'Credenciales Invalidas'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


class registrarUsuarioSistema(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "auth.view_user"
    model = User
    form_class = SignUpForm
    template_name = "usuario_sistema/alta_Usuario.html"

    def post(self, request, *args, **Kwargs):

        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                grupo = request.POST['grupo']
                print(grupo)
                user = form.save()
                group = Group.objects.get(name=grupo)
                user.groups.add(group)
                messages.success(request, 'ok'),
                return render(
                request=request,             
                template_name=self.template_name,
                context={"form": SignUpForm()},)
            else:
                 return render(
                request=request,
                template_name=self.template_name,
                context={"form": form},
            )


class editarUsuarioSistema(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "auth.view_user"
    model = User
    form_class = editUpForm
    template_name = "usuario_sistema/editar_usuario.html"
    def form_valid(self, form):
   
     self.object = form.save()
     user = form.save()
     user.groups.clear()
     group = Group.objects.get(name=self.request.POST['grupo'])
     user.groups.add(group)
     return super().form_valid(form)  

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'se gurdaron los cambios!')
        return reverse_lazy('editar_usuario_sistema',args=[self.get_object().pk])


class buscarUsuarios(LoginRequiredMixin,PermissionRequiredMixin,ListView):
      permission_required = "auth.view_user"
      model = User
      template_name = "usuario_sistema/buscar_usuarios.html"
      context_object_name = "usuarios"

      def get_queryset(self):
        
        #queryset = User.objects.select_related('auth_user_groups')
        queryset = User.objects.raw("SELECT * FROM auth_user INNER JOIN auth_user_groups ON auth_user.id=auth_user_groups.user_id INNER JOIN auth_group ON auth_group.id =auth_user_groups.group_id  where auth_group.name=  'vendedor' or auth_group.name= 'administrador' order by auth_user.id desc")
        print(queryset)
        return queryset
@login_required(login_url="/login/")
def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
