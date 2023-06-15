from django import forms
from .models import Empleado,Gerente,Desarrollador

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'salario']

class GerenteForm(forms.ModelForm):
    class Meta:
        model = Gerente
        fields = ['nombre', 'apellido', 'salario', 'departamento']

class DesarrolladorForm(forms.ModelForm):
    class Meta:
        model = Desarrollador
        fields = ['nombre', 'apellido', 'salario', 'lenguaje']