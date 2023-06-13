from django.urls import path
from . import views

app_name = 'empleados'

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('search/', views.search, name='search'),
]