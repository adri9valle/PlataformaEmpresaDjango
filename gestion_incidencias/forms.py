from django import forms

from django.forms import ModelForm
from .models import Incidencias

class FormularioIncidencias(ModelForm):
	class Meta:
		model = Incidencias
		fields = ('incidencia', 'trabajador')
		widgets = {'trabajador': forms.HiddenInput()}
	####ADD default el usuario que este con la sesion iniciada

class BuscarForm(forms.Form):
    incidencia = forms.CharField(label="")
