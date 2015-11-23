from django.shortcuts import render, redirect
#from django.http import HttpResponse

from .forms import FormularioDepartamento, FormularioPuesto, BuscarForm, FormularioPuestoMod, FormularioDepartamentoMod
from .models import Departamentos, Puestos
from gestion_empleados.models import Empleados

# Create your views here.
def add_departamento(request):
	if 'member_id' in request.session and request.session['member_id_puesto'] == "Desarrollador":
		if request.method == 'POST':
			formulario = FormularioDepartamento(request.POST)
			if formulario.is_valid():
				formulario.save()
				formulario = FormularioDepartamento()
				return render(request, 'add_departamento.html', {'formulario' : formulario , 'dep_saved' : 'ok'})
		else:
			formulario = FormularioDepartamento()
		return render(request, 'add_departamento.html', {'formulario' : formulario, 'empleado' : request.session['member_id_nombre']})
		#COMPROBAR QUE EL DEPARTAMENTO NO EXISTA
	else:
		return redirect('/')

def add_puesto(request):
	if 'member_id' in request.session and request.session['member_id_puesto'] == "Desarrollador":
		if request.method == 'POST':
			formulario = FormularioPuesto(request.POST)
			if formulario.is_valid():
				formulario.save()
				formulario = FormularioPuesto()
				return render(request, 'add_puesto.html', {'formulario' : formulario , 'pues_saved' : 'Puesto guardado correctamente'})
		else:
			formulario = FormularioPuesto()
		return render(request, 'add_puesto.html', {'formulario' : formulario, 'empleado' : request.session['member_id_nombre']})
		#COMPROBAR QUE EL PUESTO NO EXISTA
	else:
		return redirect('/')

def show_departamentos(request):
	if 'member_id' in request.session and request.session['member_id_puesto'] == "Desarrollador":
	    if request.method == 'POST':
	        formulario = BuscarForm(request.POST)
	        if formulario.is_valid():
	            #emp = formulario.cleaned_data['empleado']
	            departamentos = Departamentos.objects.all().filter(departamento__icontains=formulario.cleaned_data['nombre'])
	            formulario = BuscarForm()
	    else:
		    #Crea un formulario
		    formulario = BuscarForm()
		    # Obtiene todos los empleados
		    departamentos = Departamentos.objects.all()
		    # Devuelve los empleados los empleados // OCULTAR DNI
	    return render(request, 'show_departamentos.html', {'formulario' : formulario, 'departamentos': departamentos, 'empleado' : request.session['member_id_nombre']})
	return redirect('/')

def show_puestos(request):
	if 'member_id' in request.session and request.session['member_id_puesto'] == "Desarrollador":
	    if request.method == 'POST':
	        formulario = BuscarForm(request.POST)
	        if formulario.is_valid():
	            #emp = formulario.cleaned_data['empleado']
	            puestos = Puestos.objects.all().filter(puesto__icontains=formulario.cleaned_data['nombre'])
	            formulario = BuscarForm()
	    else:
		    #Crea un formulario
		    formulario = BuscarForm()
		    # Obtiene todos los empleados
		    puestos = Puestos.objects.all()
		    # Devuelve los empleados los empleados // OCULTAR DNI
	    return render(request, 'show_puestos.html', {'formulario' : formulario, 'puestos': puestos, 'empleado' : request.session['member_id_nombre']})
	else:
		return redirect('/')

def del_puestos(request, offset):
    #Comprobamos que haya iniciado sesion, si no se redirige al login
    if 'member_id' in request.session and request.session['member_id_puesto'] == "Desarrollador":
		offset = str(offset)
		puesto = Puestos.objects.get(puesto=offset)
		# Pedir confirmacion
		puesto.delete()
		return redirect('/show_puestos/')
		#return	render(request, 'show_empleados.html', {'emp_del' : 'ok'})
    else:
        return redirect('/')

def del_departamentos(request, offset):
    #Comprobamos que haya iniciado sesion, si no se redirige al login
    if 'member_id' in request.session and request.session['member_id_puesto'] == "Desarrollador":
		offset = str(offset)
		departamento = Departamentos.objects.get(departamento=offset)
		# Pedir confirmacion
		departamento.delete()
		return redirect('/show_departamentos/')
		#return	render(request, 'show_empleados.html', {'emp_del' : 'ok'})
    else:
        return redirect('/')