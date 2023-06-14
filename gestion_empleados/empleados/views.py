from django.shortcuts import render
from .forms import EmpleadoForm
from .models import Empleado, Gerente, Desarrollador

def index(request):
    return render(request, 'empleados/base.html')

def insert(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            nombre = data['nombre']
            apellido = data['apellido']
            salario = data['salario']
            departamento = data.get('departamento', None)
            lenguaje = data.get('lenguaje', None)

            if departamento:
                empleado = Gerente(nombre=nombre, apellido=apellido, salario=salario, departamento=departamento)
            elif lenguaje:
                empleado = Desarrollador(nombre=nombre, apellido=apellido, salario=salario, lenguaje=lenguaje)
            else:
                empleado = Empleado(nombre=nombre, apellido=apellido, salario=salario)

            empleado.save()

            return render(request, 'empleados/success.html')

    else:
        form = EmpleadoForm()

    return render(request, 'empleados/insert_form.html', {'form': form})

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
