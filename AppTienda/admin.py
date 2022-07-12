from django.contrib import admin
from AppTienda.views import productos
from .models import *


admin.site.register(Tienda)
admin.site.register(Clientes)
admin.site.register(Producto)
admin.site.register(Personal)