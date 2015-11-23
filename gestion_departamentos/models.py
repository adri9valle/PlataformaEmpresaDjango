from django.db import models

#Importamos para anadir al administrador de django
from django.contrib import admin


# Create your models here.

class Departamentos(models.Model):
	#primary key auto
	departamento = models.CharField(primary_key=True, max_length=30)
	#departamento = models.CharField(max_length=30)

	def __str__(self):
		return self.departamento

class Puestos(models.Model):
	#primary key auto
	puesto = models.CharField(primary_key=True, max_length=30)
	#puesto = models.CharField(max_length=30)
	departamento = models.ForeignKey(Departamentos)
	
	def __str__(self):
		return self.puesto

admin.site.register(Departamentos)
admin.site.register(Puestos)