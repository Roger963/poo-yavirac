from django.contrib import admin
from datosFactura.models import Factura, Detalle
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('cliente_id', 'fecha')

class DetalleAdmin(admin.ModelAdmin):
    list_display = ('factura_id', 'product_id', 'cantidad', 'precio')

admin.site.register(Factura, FacturaAdmin)
admin.site.register(Detalle,DetalleAdmin)
