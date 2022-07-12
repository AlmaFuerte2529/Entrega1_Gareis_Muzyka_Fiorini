from django import http
from django.shortcuts import render
from .models import Tienda
from django.http import HttpResponse
#from AppTienda.forms import FormClientes


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
        nombrecompleto= request.POST.get("nombrecompleto")
        dni= request.POST.get("dni")
        edad= request.POST.get("edad")
        direccion= request.POST.get("direccion")
        cp= request.POST.get("cp")
        email= request.POST.get("email")
        telefono= request.POST.get("telefono")
        cliente= clientes(nombrecompleto=nombrecompleto, dni=dni, edad=edad, direccion=direccion, cp=cp, email=email, telefono=telefono)
        cliente.save()
        return render (request, "AppTienda/inicio.html")
        

    return render(request, "AppTienda/formClientes.html")