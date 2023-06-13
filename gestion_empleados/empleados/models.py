from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=8, decimal_places=2)

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def obtener_salario_anual(self):
        return self.salario * 12


class Gerente(Empleado):
    departamento = models.CharField(max_length=100)

    def obtener_informacion_departamento(self):
        return f"Departamento: {self.departamento}"


class Desarrollador(Empleado):
    lenguaje = models.CharField(max_length=100)

    def obtener_lenguaje(self):
        return f"Lenguaje: {self.lenguaje}"
# Create your models here.
