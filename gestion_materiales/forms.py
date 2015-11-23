from django import forms

from django.forms import ModelForm
from .models import Materiales

class FormularioMateriales(ModelForm):

	class Meta:
		model = Materiales
#######ADD accion para formulario de modificar	

class BuscarForm(forms.Form):
    material = forms.CharField(label="")

class FormularioMaterialMod(ModelForm):
	# ESCONDER DNI
	class Meta:
		model = Materiales
		fields = ('material', 'trabajador',)