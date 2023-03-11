from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Auto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return self.modelo

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    codigopostal = models.IntegerField()

    def __str__(self):
        return self.codigopostal
