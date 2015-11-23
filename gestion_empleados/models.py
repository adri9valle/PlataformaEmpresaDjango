from django.db import models
from django.contrib import admin

# Create your models here.

#Importamos otros modelos 
from gestion_departamentos.models import Puestos

class Empleados(models.Model):
	dni = models.CharField(max_length=9 ,primary_key=True)
	nombre = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=40)
	telefono = models.IntegerField(max_length=9)
	direccion = models.CharField(max_length=60)
	correo = models.CharField(max_length=30)
	horario = models.CharField(max_length=30)
	salario =  models.IntegerField()
	puesto = models.ForeignKey(Puestos)

	def __str__(self):
		return self.nombre + " " + self.dni

class CalendarioLaboral(models.Model):
	fecha = models.DateField(auto_now=True, auto_now_add=True)
	trabajador = models.ForeignKey(Empleados) 
	asistencia =  models.BooleanField(default=1)

	def __str__(self):
		return self.trabajador.apellidos

class ArchivoCarga(models.Model):
	archivo = models.FileField(upload_to='media/')

admin.site.register(CalendarioLaboral)