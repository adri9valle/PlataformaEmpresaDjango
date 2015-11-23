from django import forms
from django.forms import ModelForm

from .models import Departamentos, Puestos

class FormularioDepartamento(ModelForm):

	class Meta:
		model = Departamentos

class FormularioPuesto(ModelForm):

	class Meta:
		model = Puestos

class BuscarForm(forms.Form):
    nombre = forms.CharField(label="")

class FormularioPuestoMod(ModelForm):
	# ESCONDER DNI
	class Meta:
		model = Puestos
		fields = ('puesto',)

class FormularioDepartamentoMod(ModelForm):
	# ESCONDER DNI
	class Meta:
		model = Departamentos
		fields = ('departamento',)