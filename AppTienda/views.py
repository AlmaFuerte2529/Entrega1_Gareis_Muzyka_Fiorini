from django import http
from django.shortcuts import render, HttpResponse
from AppTienda.models import Tienda, Clientes, Personal, Producto
from django.http import HttpResponse
from AppTienda.forms import FormClientes, FormPersonal, FormProducto


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

def formPersonal(request):

    if (request.method=="POST"):
        form= FormPersonal(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombrecompleto= info["nombrecompleto"]
            dni= info["dni"]
            direccion= info["direccion"]
            cargo= info["cargo"]
            telefono= info["telefono"]
            usuario= info["usuario"]
            clave= info["clave"]
            personal= Personal(nombrecompleto=nombrecompleto, dni=dni, direccion=direccion, telefono=telefono, cargo=cargo, usuario=usuario, clave=clave)
            personal.save()
            return render(request, "AppTienda/inicio.html")
    else:
         form= FormPersonal()
    
    return render(request, "AppTienda/formPersonal.html", {"formulario":form})

def formProducto(request):

    if (request.method=="POST"):
        form= FormProducto(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            codigo= info["codigo"]
            articulo= info["articulo"]
            precio= info["precio"]
            fechaingreso= info["fechaingreso"]
            stock= info["stock"]
            disponible= info["disponible"]
            productos= Producto(codigo=codigo, articulo=articulo, precio=precio, fechaingreso=fechaingreso, stock=stock, disponible=disponible)
            productos.save()
            return render(request, "AppTienda/inicio.html")
    else:
         form= FormProducto()
    
    return render(request, "AppTienda/formProducto.html", {"formulario":form})    

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