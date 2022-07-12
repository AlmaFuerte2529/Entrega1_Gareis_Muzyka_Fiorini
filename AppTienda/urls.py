from django.urls import path
from .views import *


urlpatterns = [
    path('tienda/', tienda),
    path('clientes/', clientes),
    path('productos/', productos),
    path('personal/', personal),
    path('', inicio),
]
