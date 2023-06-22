from django.urls import path
from empleados import views

app_name = 'empleados'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

#Empleado

    path('empleado/', views.ListadoEmpleados.as_view(), name='listado_empleados'),
    path('crear-empleado/', views.CrearEmpleado.as_view(), name='crear_empleado'),
    path('editar-empleado/<int:pk>/', views.EditarEmpleado.as_view(), name='editar_empleado'),
    path('eliminar-empleado/<int:pk>/', views.EliminarEmpleado.as_view(), name='eliminar_empleado'),
    path('mostrar-empleado/<int:pk>/', views.MostrarEmpleado.as_view(), name='mostrar_empleado'),

#Gerente

    path('gerentes/', views.ListadoGerentes.as_view(), name='listado_gerentes'),
    path('crear-gerente/', views.CrearGerente.as_view(), name='crear_gerente'),
    path('editar-gerente/<int:pk>/', views.EditarGerente.as_view(), name='editar_gerente'),
    path('eliminar-gerente/<int:pk>/', views.EliminarGerente.as_view(), name='eliminar_gerente'),
    path('mostrar-gerente/<int:pk>/', views.MostrarGerente.as_view(), name='mostrar_gerente'),

#Desarrollador

    path('desarrolladores/', views.ListadoDesarrolladores.as_view(), name='listado_desarrolladores'),
    path('crear-desarrollador/', views.CrearDesarrollador.as_view(), name='crear_desarrollador'),
    path('editar-desarrollador/<int:pk>/', views.EditarDesarrollador.as_view(), name='editar_desarrollador'),
    path('eliminar-desarrollador/<int:pk>/', views.EliminarDesarrollador.as_view(), name='eliminar_desarrollador'),
    path('mostrar-desarrollador/<int:pk>/', views.MostrarDesarrollador.as_view(), name='mostrar_desarrollador'),
]