from django.db import models

#Importamos para anadir al administrador de django
from django.contrib import admin

#Importamos otros modelos 
from gestion_empleados.models import Empleados

# Create your models here.

class Materiales(models.Model):
	etiqueta = models.CharField(max_length=10 ,primary_key=True)
	### HACER FK trabajador que pueda ser nula
	trabajador = models.ForeignKey(Empleados, blank=True, null=True) 
	material = models.CharField(max_length=30)

	def __str__(self):
		return self.material + " / " + self.etiqueta

admin.site.register(Materiales)
admin.site.register(Empleados)
