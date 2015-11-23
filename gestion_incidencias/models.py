from django.db import models

# Create your models here.

#Importamos otros modelos necesarios
from gestion_empleados.models import Empleados

#Importamos para anadir al administrador de django
from django.contrib import admin


# Create your models here.

class Incidencias(models.Model):
	incidencia = models.TextField()
	fecha = models.DateField(auto_now=True, auto_now_add=True)
	trabajador = models.ForeignKey(Empleados)
	
	def __str__(self):
		return self.incidencia


admin.site.register(Incidencias)