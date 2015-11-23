from django import forms
from django.forms import ModelForm

from .models import Empleados, ArchivoCarga

#import datetime

class BuscarEmpleadoForm(forms.Form):
    empleado = forms.CharField(label="")

class FormularioEmpleado(ModelForm):

	class Meta:
		model = Empleados
		fields = '__all__'
		
class FormularioEmpleadoMod(ModelForm):
	# ESCONDER DNI
	class Meta:
		model = Empleados
		fields = ('apellidos', 'telefono', 'direccion', 'correo', 'horario', 'nombre', 'salario', 'puesto')

class SubirArchivoForm(ModelForm):

	class Meta:
		model = ArchivoCarga
		
class CalendarioForm(forms.Form):
	opciones = (
    ('dia', 'Day'),
    ('mes', 'Month'),
    ('ano', 'Year'),
    )
	num = forms.IntegerField(label="Introduce Numero")
	opcion = forms.ChoiceField(choices=opciones)