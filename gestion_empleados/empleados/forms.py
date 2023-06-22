from django import forms
from .models import Gerente,Desarrollador

class GerenteForm(forms.ModelForm):
    class Meta:
        model = Gerente
        fields = ('nombre', 'apellido', 'salario', 'departamento')

class DesarrolladorForm(forms.ModelForm):
    class Meta:
        model = Desarrollador
        fields = ('nombre', 'apellido', 'salario', 'lenguaje')

class BusquedaForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=False)
    apellido = forms.CharField(label='Apellido', required=False)
