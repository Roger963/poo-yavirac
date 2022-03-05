from django.db import models
from datosBasicos.models import Product, Cliente


class Factura(models.Model):
    cliente_id = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()


class Detalle(models.Model):
    factura_id = models.ForeignKey(Factura, on_delete=models.CASCADE)
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
