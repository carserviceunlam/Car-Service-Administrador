from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Cliente
from django.views.generic import CreateView, UpdateView
from apps.personas.models import Persona
from apps.ubicacion.models import Ciudad
from apps.servicios.models import BD
from django.contrib.auth.decorators import login_required
from .forms import registerForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


@login_required(login_url="/login/")
def altaClientes(request):
    ciudad = Ciudad.objects.all()
    data = {'form': registerForm()}
    context = {}
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            business_name = form.cleaned_data.get('business_name')
            cuit_cuil = 123
            city_id = 1
            email = 32
            cliente = Cliente.objects.create(
                business_name=business_name, cuit_cuil=cuit_cuil, email=email, city_id_id=city_id)
            return redirect('/editarClientes/1')
        else:

            template_name = "home/altaClientes.html"
            return render(request, template_name, {'form': form})
    else:
        return render(request, "home/altaClientes.html", data)


class registrarCliente(CreateView):

    model = Cliente
    form_class = registerForm
    template_name = "clientes/alta_cliente.html"

    def post(self, request, *args, **Kwargs):

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
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
                response.status_code = 400
                return response
           


class editarCliente(LoginRequiredMixin,UpdateView):

    model = Cliente
    form_class = registerForm
    template_name = "clientes/editar_cliente.html"

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


def eliminarCliente(request, id):

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        ClienteDelete = Cliente.objects.get(id=id)
        if (ClienteDelete):
            ClienteDelete.delete()
            mensaje ='eliminado Correctamente'
            error = 'no hay error'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            mensaje = 'no se pudo eliminar'
            error = "error"
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 400
            return response
    else:
        return ClienteDelete

def get_ciudad_bd(_request, id):


    if (Cliente.objects.filter(id=id).first()):
        cliente = Cliente.objects.filter(id=id).first()
        if(BD.objects.filter(customer_id=cliente.id).first()):
          data = {'message': "Success", 'cliente': cliente.bd.name_bd+"_"}
        else:
          data = {'message': "Success",'cliente': "Cliente sin BD asignado"}
    else:
        data = {'message': "Success", 'cliente':"cliente no encontrado"}

    return JsonResponse(data)


@login_required(login_url="/login/")
def editarClientes(request, id):
    cliente = Cliente.objects.get(id=id)
    persona = Persona.objects.filter(customer_id=id)
    bd = BD.objects.filter(customer_id=id)
    ciudad = Ciudad.objects.all()
    return render(request, "home/editarClientes.html", {"cliente": cliente, "persona": persona, "ciudad": ciudad, "bd": bd})


@login_required(login_url="/login/")
def buscarClientes(request):
    cliente = Cliente.objects.all()
    return render(request, "home/buscarClientes.html", {"cliente": cliente})
