import email
from django import forms

class FormClientes(forms.Form):
    nombrecompleto = forms.CharField(max_length=50)
    dni = forms.IntegerField()
    edad = forms.IntegerField()
    direccion = forms.CharField(max_length=50)
    cp = forms.IntegerField()
    email = forms.EmailField()
    telefono = forms.IntegerField()

class FormPersonal(forms.Form):
    dni = forms.IntegerField()
    usuario = forms.CharField(max_length=50)
    clave = forms.CharField(max_length=50)
    nombrecompleto = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)
    telefono = forms.IntegerField()
    cargo = forms.CharField(max_length=50)

class FormProducto(forms.Form):
    codigo = forms.IntegerField()
    articulo = forms.CharField(max_length=50)
    precio = forms.IntegerField()
    fechaingreso = forms.DateField()
    stock = forms.IntegerField()
    disponible = forms.BooleanField()