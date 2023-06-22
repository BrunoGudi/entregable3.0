from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.http import HttpRequest
from empleados.models import Empleado,Gerente,Desarrollador
from empleados.forms import GerenteForm, DesarrolladorForm, BusquedaForm

# Create your views here.

# clase Empleados

class ListadoEmpleados(ListView):
    model = Empleado
    template_name = 'empleados/listar_empleado.html'

class CrearEmpleado(CreateView):
    model = Empleado
    template_name = 'empleados/crear_empleado.html'
    success_url = reverse_lazy('empleados:listado_empleados')
    fields = ['nombre', 'apellido', 'salario']

class EditarEmpleado(UpdateView):
    model = Empleado
    template_name = 'empleados/editar_empleado.html'
    fields = ['nombre', 'apellido', 'salario']
    pk_url_kwarg = 'pk'

    def get_success_url(self) -> str:
        request: HttpRequest = self.request
        domain = request.META['HTTP_HOST']
        return f"http://{domain}/empleados/mostrar-empleado/{self.object.pk}/"


class EliminarEmpleado(DeleteView):
    model = Empleado
    template_name = 'empleados/eliminar_empleado.html'
    pk_url_kwarg = 'pk'

    def get_success_url(self) -> str:
        request: HttpRequest = self.request
        domain = request.META['HTTP_HOST']
        return f"http://{domain}/empleados"

class MostrarEmpleado(DetailView):
    model = Empleado
    template_name = 'empleados/mostrar_empleado.html'

#### clase Gerente

class ListadoGerentes(ListView):
    model = Gerente
    template_name = 'gerentes/listar_gerente.html'

class CrearGerente(CreateView):
    model = Gerente
    template_name = 'gerentes/crear_gerente.html'
    form_class = GerenteForm
    success_url = reverse_lazy('empleados:listado_gerentes')

class EditarGerente(UpdateView):
    model = Gerente
    template_name = 'gerentes/editar_gerente.html'
    fields = ('nombre', 'apellido', 'salario', 'departamento')
    pk_url_kwarg = 'pk'

    def get_success_url(self) -> str:
        request = self.request
        domain = request.META['HTTP_HOST']
        return f"http://{domain}/empleados/mostrar-gerente/{self.object.pk}/"

class EliminarGerente(DeleteView):
    model = Gerente
    template_name = 'gerentes/eliminar_gerente.html'
    success_url = reverse_lazy('empleados:listado_gerentes')

class MostrarGerente(DetailView):
    model = Gerente
    template_name = 'gerentes/mostrar_gerente.html'


#### clase Desarrollador

class ListadoDesarrolladores(ListView):
    model = Desarrollador
    template_name = 'desarrolladores/listar_desarrollador.html'


class CrearDesarrollador(CreateView):
    model = Desarrollador
    template_name = 'desarrolladores/crear_desarrollador.html'
    form_class = DesarrolladorForm
    success_url = reverse_lazy('empleados:listado_desarrolladores')



class EditarDesarrollador(UpdateView):
    model = Desarrollador
    template_name = 'desarrolladores/editar_desarrollador.html'
    fields = ('nombre', 'apellido', 'salario', 'lenguaje')
    pk_url_kwarg = 'pk'

    def get_success_url(self) -> str:
        request = self.request
        domain = request.META['HTTP_HOST']
        return f"http://{domain}/empleados/mostrar-desarrollador/{self.object.pk}/"


class EliminarDesarrollador(DeleteView):
    model = Desarrollador
    template_name = 'desarrolladores/eliminar_desarrollador.html'
    success_url = reverse_lazy('empleados:listado_desarrolladores')


class MostrarDesarrollador(DetailView):
    model = Desarrollador
    template_name = 'desarrolladores/mostrar_desarrollador.html'


def index(request):
    return render(request, 'empleados/base.html')


def search(request):
    form = BusquedaForm(request.GET)
    resultados = []

    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']

        empleados = Empleado.objects.filter(nombre__icontains=nombre, apellido__icontains=apellido)
        gerentes = Gerente.objects.filter(nombre__icontains=nombre, apellido__icontains=apellido)
        desarrolladores = Desarrollador.objects.filter(nombre__icontains=nombre, apellido__icontains=apellido)

        resultados.extend(empleados)
        resultados.extend(gerentes)
        resultados.extend(desarrolladores)

    return render(request, 'empleados/search_form.html', {'form': form, 'resultados': resultados})



