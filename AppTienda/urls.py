from django.urls import path
from .views import *


urlpatterns = [
    path('tienda/', tienda),
    path('clientes/', clientes, name= 'clientes'),
    path('productos/', productos, name= 'productos'),
    path('personal/', personal, name= 'personal'),
    path('', inicio, name= 'inicio'),
    path('formClientes/', formClientes, name='formClientes'),
    path('formPersonal/', formPersonal, name='formPersonal'),
    path('formProducto/', formProducto, name='formProducto'),
    path('buscaCliente/', buscaCliente, name= 'buscaCliente'),
    path('personal/list', PersonalList.as_view(), name='personal_listar'),



]
