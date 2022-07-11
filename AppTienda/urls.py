#Importo path para las urls
from django.urls import path
#importo todas las vistas
from .views import *

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('clientes/', clientes, name='clientes'),
    path('personal/', personal, name='Personal'),
    path('productos/', productos, name='Productos'),
]