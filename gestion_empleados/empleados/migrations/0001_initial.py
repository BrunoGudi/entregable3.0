# Generated by Django 4.1.3 on 2023-06-21 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=100)),
                ('apellido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gerente_apellido', to='empleados.empleado')),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gerente_nombre', to='empleados.empleado')),
                ('salario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gerente_salario', to='empleados.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Desarrollador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lenguaje', models.CharField(max_length=100)),
                ('apellido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desarrollador_apellido', to='empleados.empleado')),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desarrollador_nombre', to='empleados.empleado')),
                ('salario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desarrollador_salario', to='empleados.empleado')),
            ],
        ),
    ]
