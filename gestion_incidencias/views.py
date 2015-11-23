from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from django.db import connection

from .models import Incidencias
from .forms import FormularioIncidencias, BuscarForm

# Create your views here.

######TEMPORAL, SOLUCIONAR ERROR CARACTERES##############
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
#################################

def add_incidencia(request):
	if 'member_id' in request.session:
		# si el usuario esta enviando el formulario con datos
		if request.method == 'POST': 
			# Bound form
			formulario = FormularioIncidencias(request.POST) 
			if formulario.is_valid():
				# Guardar los datos en la base de datos
		   		formulario.save() 
		   		#return HttpResponse("Empleado guardado")
		   		formulario = FormularioIncidencias()
		   		return render(request, 'add_incidencia.html', {'formulario' : formulario, 'inci_saved' : 'ok'})
		else:
		    formulario = FormularioIncidencias(initial={'trabajador':request.session['member_id']})

		if request.session['member_id_puesto'] != 'Desarrollador':
			return render(request, 'add_incidencia_user.html', {'formulario' : formulario, 'trabajador' : request.session['member_id'] , 'empleado' : request.session['member_id_nombre']})
		else:
			return render(request, 'add_incidencia.html', {'formulario' : formulario, 'trabajador' : request.session['member_id'] , 'empleado' : request.session['member_id_nombre']})
	else:
		return redirect('/')

def show_incidencias(request):
	if 'member_id' in request.session and request.session['member_id_puesto'] == "Desarrollador":
	    if request.method == 'POST':
	        formulario = BuscarForm(request.POST)
	        if formulario.is_valid():
	            #emp = formulario.cleaned_data['empleado']
	            incidencias = Incidencias.objects.all().filter(incidencia__icontains=formulario.cleaned_data['incidencia'])
	            formulario = BuscarForm()
	    else:
		    #Crea un formulario
		    formulario = BuscarForm()
		    # Obtiene todos los empleados
		    incidencias = Incidencias.objects.all()
		    # Devuelve los empleados los empleados // OCULTAR DNI
	    return render(request, 'show_incidencias.html', {'formulario' : formulario, 'incidencias': incidencias, 'empleado' : request.session['member_id_nombre']})
	else:
		return redirect('/')

def del_incidencias(request, offset):
	if 'member_id' in request.session and request.session['member_id_puesto'] == "Desarrollador":
		offset = int(offset)
		incidencia = Incidencias.objects.get(pk=offset)
		# Pedir confirmacion
		incidencia.delete()
		return redirect('/show_incidencias/')
	return redirect('/')