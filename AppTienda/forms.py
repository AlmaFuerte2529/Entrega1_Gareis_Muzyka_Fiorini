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
