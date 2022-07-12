from django.db import models

class Tienda(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


#--->Clase Cliente
class Clientes(models.Model):
    #entero
    dni= models.IntegerField()
    #string
    nombrecompleto= models.CharField(max_length=50)
    #entero
    edad=models.IntegerField()
    #string
    direccion=models.CharField(max_length=50)
    #int
    cp=models.IntegerField()
    #email
    email=models.EmailField()
    #entero
    telefono=models.IntegerField()

#--->Clase Productos
class Producto(models.Model):
    codigoarticulo=models.IntegerField()
    articulo=models.CharField(max_length=50)
    #decimal -->cambiar
    precio=models.IntegerField()
    #datetime
    fechaingreso=models.DateField()
    #int
    stock= models.IntegerField()
    #booleano --- > Activo/Inactivo
    disponible=models.BooleanField()

#--->Clase Personal
class Personal(models.Model):
    dni=models.IntegerField()
    #usuario -->futuro login
    usuario=models.CharField(max_length=50)
    #clave --> futuro login
    clave= models.CharField(max_length=50)
    nombrecompleto=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    telefono=models.IntegerField()
    cargo=models.CharField(max_length=50)
