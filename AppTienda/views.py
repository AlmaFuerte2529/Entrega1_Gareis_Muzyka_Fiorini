from django import http
from django.shortcuts import render, HttpResponse
from AppTienda.models import Tienda, Clientes
from django.http import HttpResponse
from AppTienda.forms import FormClientes


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
        form= FormClientes(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombrecompleto= info["nombrecompleto"]
            dni= info["dni"]
            edad= info["edad"]
            direccion= info["direccion"]
            cp= info["cp"]
            email= info["email"]
            telefono= info["telefono"]
            cliente= Clientes(nombrecompleto=nombrecompleto, dni=dni, edad=edad, direccion=direccion, cp=cp, email=email, telefono=telefono)
            cliente.save()
            return render(request, "AppTienda/inicio.html")
    else:
         form= FormClientes()
    
    return render(request, "AppTienda/formClientes.html", {"formulario":form})

def buscaCliente(request):
    try:
        if request.GET["nombrecompleto"]:
            cliente = request.GET["nombrecompleto"]
            clientes=Clientes.objects.filter(nombrecompleto__icontains=cliente)
            if clientes:
                return render(request, "AppTienda/buscaCliente.html", {"clientes":clientes})
            else:
                return render(request, "AppTienda/buscaCliente.html", {"error":"No hay clientes con ese nombre"})
        elif request.GET["nombrecompleto"] == "":
            return render(request, "AppTienda/buscaCliente.html", {"error":"No se ingreso ningun nombre"})
    except:
        return render(request, "AppTienda/buscaCliente.html")