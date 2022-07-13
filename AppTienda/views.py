from django import http
from django.shortcuts import render
from .models import Tienda
from .models import Clientes
from django.http import HttpResponse
#from AppTienda.forms import formClientes


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

def formClientes(request):

    if (request.method=="POST"):
        form= formClientes(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombrecompleto= info["nombrecompleto"]
            dni= info["dni"]
            edad= info["edad"]
            direccion= info["direccion"]
            cp= info["cp"]
            datos= Clientes(nombrecompleto=nombrecompleto, dni=dni,edad=edad,direccion=direccion,cp=cp)
            datos.save()
            
            
            
    return render(request, "AppTienda/formClientes.html")

