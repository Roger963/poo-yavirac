from django.db import models

# Create your models here.
class Product(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.IntegerField()


class Cliente(models.Model):
    name = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    fecha_nacimiento = models.DateTimeField(auto_now_add=True)
    telefono = models.IntegerField()
    email = models.EmailField()
    categoria = models.CharField(max_length=200)


