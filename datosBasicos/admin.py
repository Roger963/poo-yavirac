from django.contrib import admin
from datosBasicos.models import Product, Cliente


class ProductAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'apellido', 'direccion', 'fecha_nacimiento', 'telefono', 'email', 'categoria')
    
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Cliente, ClienteAdmin)

