from django import http
from django.shortcuts import render
from AppTienda.models import Tienda
from django.http import HttpResponse


def tienda(self):
    
    tienda= Tienda(nombre= "Mi Tienda")
    tienda.save()


#--->Inicio
def inicio(request):
    return render(request, "AppTienda/inicio.html")

#--->Personal
def personal(request):
    return render(request, "AppTienda/personal.html")

#--->Productos
def productos(request):
    return render(request, "AppTienda/productos.html")

#--->Clientes
def clientes(request):
    return render(request, "AppTienda/clientes.html")