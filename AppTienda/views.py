from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

#Creamos las Vistas

#--->Inicio

def inicio(request):
    return render (request, "AppTienda/inicio.html")

#--->Personal
def personal(request):
    return render (request, "AppTienda/Personal.html")

#--->Productos
def productos(request):
    return render (request, "AppTienda/Productos.html")

#--->Clientes
def clientes(request):
    return render (request, "AppTienda/clientes.html")