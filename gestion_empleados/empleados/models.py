from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=8, decimal_places=2)

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def obtener_salario_anual(self):
        return {self.salario}


class Gerente(models.Model):
    nombre = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='gerente_nombre')
    apellido = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='gerente_apellido')
    salario = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='gerente_salario')
    departamento = models.CharField(max_length=100)

    def obtener_informacion_departamento(self):
        return f"Departamento: {self.departamento}"


class Desarrollador(models.Model):
    nombre = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='desarrollador_nombre')
    apellido = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='desarrollador_apellido')
    salario = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='desarrollador_salario')
    lenguaje = models.CharField(max_length=100)

    def obtener_lenguaje(self):
        return f"Lenguaje: {self.lenguaje}"
# Create your models here.
