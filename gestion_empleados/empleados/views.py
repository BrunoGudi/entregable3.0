from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from empleados.models import Empleado,Gerente,Desarrollador

def index(request):
    return render(request, 'empleados/base.html')

# clase Empleados

class ListadoEmpleados(ListView):
    model = Empleado
    templane_name = 'empleados/listar_empleado.html'

class CrearEmpleado(CreateView):
    model = Empleado
    template_name = 'empleados/crear_empleado.html'
    success_url = reverse_lazy('listado_empleados')
    fields = 'nombre', 'apellido', 'salario'

class EditarEmpleado(UpdateView):
    model = Empleado
    template_name = 'empleados/editar_empleado.html'
    fields = 'nombre', 'apellido', 'salario'

    def get_success_url(self) -> str:
        return reverse_lazy('mostrar_empleado', kwargs={'pk':self.object.pk})

class EliminarEmpleado(DeleteView):
    model = Empleado
    template_name = 'empleados/eliminar_empleado.html'
    success_url = reverse_lazy('listado_empleados')

class MostrarEmpleado(DetailView):
    model = Empleado
    template_name = 'empleados/mostrar_empleado.html'

#### clase Gerente

class ListadoGerentes(ListView):
    model = Gerente
    templane_name = 'empleados/listar_gerente.html'

class CrearGerente(CreateView):
    model = Gerente
    template_name = 'empleados/crear_gerente.html'
    success_url = reverse_lazy('listado_gerente')
    fields = ('nombre', 'apellido', 'salario', 'departamento')

class EditarGerente(UpdateView):
    model = Gerente
    template_name = 'empleados/editar_gerente.html'
    fields = ('nombre', 'apellido', 'salario', 'departamento')

    def get_success_url(self) -> str:
        return reverse_lazy('mostrar_gerente', kwargs={'pk':self.object.pk})

class EliminarGerente(DeleteView):
    model = Gerente
    template_name = 'empleados/eliminar_gerente.html'
    success_url = reverse_lazy('listado_gerente')

class MostrarGerente(DetailView):
    model = Gerente
    template_name = 'empleados/mostrar_gerente.html'

#### clase Desarrollador

class ListadoDesarrolladores(ListView):
    model = Desarrollador
    templane_name = 'empleados/listar_desarrollador.html'

class CrearDesarrollador(CreateView):
    model = Desarrollador
    template_name = 'empleados/crear_desarrollador'
    success_url = reverse_lazy('listado_desarrollador')
    # fields = 'nombre', 'apellido', 'salario', 'lenguaje'

class EditarDesarrollador(UpdateView):
    model = Desarrollador
    template_name = 'empleados/editar_desarrollador'
    # fields = 'nombre', 'apellido', 'salario', 'lenguaje'

    def get_success_url(self) -> str:
        return reverse_lazy('mostrar_desarrollador', kwargs={'pk':self.object.pk})

class EliminarDesarrollador(DeleteView):
    model = Desarrollador
    template_name = 'empleados/eliminar_desarrolladoro.html'
    success_url = reverse_lazy('listado_desarrollador')

class MostrarDesarrollador(DetailView):
    model = Desarrollador
    template_name = 'empleados/mostrar_desarrollador.html'







def search(request):
    term = request.GET.get('term')
    resultados = []

    if term:
        empleados = Empleado.objects.filter(nombre__icontains=term) | \
                    Empleado.objects.filter(apellido__icontains=term)

        for empleado in empleados:
            resultados.append(empleado)

    return render(request, 'empleados/search_form.html', {'term': term, 'resultados': resultados})

# Create your views here.
