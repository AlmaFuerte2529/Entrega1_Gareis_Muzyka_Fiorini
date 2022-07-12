from django.urls import path
from .views import *


urlpatterns = [
    path('tienda/', tienda),
    path('clientes/', clientes, name= 'clientes'),
    path('productos/', productos, name= 'productos'),
    path('personal/', personal, name= 'personal'),
    path('', inicio, name= 'inicio'),
]
