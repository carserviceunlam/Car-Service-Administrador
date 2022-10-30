from this import d
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.modulos.models import modules, module_segmentacion, customer_modules
from django.views.generic import CreateView, UpdateView, ListView
from .forms import registroModulo, registroSegmentacion, asignarModulos
from apps.clientes.models import Cliente, cliente_user
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.


class registrarModulo(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "modulos.view_modules"
    model = modules
    form_class = registroModulo
    template_name = "modulos/alta_modulos.html"

    def post(self, request, *args, **Kwargs):

        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                modulo = form.save()
                return redirect('/editar/modulo/' + str(modulo.id))
            else:
                return render(
                    request=request,
                    template_name=self.template_name,
                    context={"form": form},
                )


class editarModulo(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "modulos.view_modules"
    model = modules
    form_class = registroModulo
    template_name = "modulos/editar_modulos.html"

    def get_success_url(self):
        return reverse_lazy('editar_modulo', args=[self.get_object().pk])


class registrarPlan(LoginRequiredMixin,PermissionRequiredMixin,CreateView):

    permission_required = "modulos.view_module_segmentacion"
    model = module_segmentacion
    form_class = registroSegmentacion
    template_name = "modulos_planes/alta_plan.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def post(self, request, *args, **Kwargs):

        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                modulo = form.save()
                return redirect('/editar/Plan/' + str(modulo.id))
            else:
                return render(
                    request=request,
                    template_name=self.template_name,
                    context={"form": form},
                )


class editarPlan(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "modulos.view_module_segmentacion"
    model = module_segmentacion
    form_class = registroSegmentacion
    template_name = "modulos_planes/editar_plan.html"

    def get_success_url(self):
        return reverse_lazy('editar_plan', args=[self.get_object().pk])


class asignarModulos(LoginRequiredMixin,CreateView):
    model = customer_modules
    form_class = asignarModulos
    template_name = "modulos/modulos_clientes_agregar.html"

    def post(self, request, *args, **Kwargs):

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                modules = form.save()
                print(form.cleaned_data.get('module_segmentacion_id'))
                print(form.cleaned_data.get('customer_id'))
                usuario = cliente_user.objects.filter(
                    customer_id=form.cleaned_data.get('customer_id'))
                if (usuario):
                    for u in usuario:
                        print(u)
                        for m in modules.module_segmentacion_id.module_id.all():
                         print(m.codigo)
                         permission = Permission.objects.get(codename=m.codigo)
                         u.user_id.user_permissions.add(permission)

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


def retirarModulos(request, id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        plan = customer_modules.objects.get(id=id)
        if (plan):
            cliente = Cliente.objects.get(id=plan.customer_id.id)
            usuario = cliente_user.objects.filter(customer_id=cliente.id)
            planVigente = customer_modules.objects.filter(
                customer_id=cliente.id)
            plan.delete()
            for u in usuario:
                print(u.user_id.user_permissions.clear())
                for p in planVigente:
                    for m in p.module_segmentacion_id.module_id.all():
                        permission = Permission.objects.get(codename=m.codigo)
                        u.user_id.user_permissions.add(permission)

            mensaje = 'eliminado Correctamente'
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
        d


def moduloSegmentacion(request):
    form_class = registroModulo
    template_name = "modulos/editar_modulos.html"
    modulo = modules.objects.get(id=id)
    if request.method == "POST":
        form = registroModulo(request.POST, instance=modulo)
        if form.is_valid():
            form.save()
            return redirect('/editar/modulo/' + str(id))
        else:
            data = {'form': form}
            return render(
                request,
                "modulos/editar_modulos.html",
                data
            )
    else:
        data = {'form': registroModulo(instance=modulo)}

        return render(request, template_name, data)


@login_required(login_url="/login/")
def buscarModulos(request):
    template_name = "modulos/buscar_modulos.html"
    modulos = modules.objects.all().order_by('-id')
    print(modulos)
    return render(request, template_name, {"modulos": modulos})


class buscarPlanes(LoginRequiredMixin,ListView):
    model = module_segmentacion
    template_name = "modulos_planes/buscar_planes.html"
    context_object_name = "planes"

    def get_queryset(self):

        queryset = module_segmentacion.objects.all().order_by('-id')
        return queryset
