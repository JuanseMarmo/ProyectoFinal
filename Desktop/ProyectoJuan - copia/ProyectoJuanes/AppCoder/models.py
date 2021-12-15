from django.db import models

# Create your models here.
class Auto(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    anio = models.IntegerField()

    def __str__(self):

        return f"Marca: {self.marca} / Modelo: {self.modelo} / Año: {self.anio}"

class Moto(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    anio = models.IntegerField()

    def __str__(self):

        return f"Marca: {self.marca} / Modelo: {self.modelo} / Año: {self.anio}"

class Camion(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    anio = models.IntegerField()

    def __str__(self):

        return f"Marca: {self.marca} / Modelo: {self.modelo} / Año: {self.anio}"

class Vender(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    anio = models.IntegerField()

    def __str__(self):

        return f"Marca: {self.marca} / Modelo: {self.modelo} / Año: {self.anio}"

