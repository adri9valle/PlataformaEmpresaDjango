from django.shortcuts import render,redirect
#from django.http import HttpResponse

#from .models import Materiales
from .forms import FormularioMateriales, BuscarForm, FormularioMaterialMod
from .models import Materiales
from gestion_empleados.models import Empleados

# Create your views here.


def add_material(request):
	if 'member_id' in request.session and request.session['member_id_puesto'] == "Desarrollador":
		# si el usuario esta enviando el formulario con datos
		######TEMPORAL, SOLUCIONAR ERROR CARACTERES##############
		import sys
		reload(sys)
		sys.setdefaultencoding("utf-8")
		#################################
		if request.method == 'POST': 
			# Bound form
			formulario = FormularioMateriales(request.POST) 
			if formulario.is_valid():
				# Guardar los datos en la base de datos
		   		formulario.save() 
		   		#return HttpResponse("Material guardado")
		   		formulario = FormularioMateriales()
		   		return render(request, 'add_material.html', {'formulario' : formulario, 'mate_saved' : 'ok', 'empleado' : request.session['member_id_nombre']})
		else:
		    formulario = FormularioMateriales()
		return render(request, 'add_material.html', {'formulario': formulario, 'empleado' : request.session['member_id_nombre']})
	else:
		return redirect('/')

def show_materiales(request):
	if 'member_id' in request.session and request.session['member_id_puesto'] == "Desarrollador":
	    if request.method == 'POST':
	        formulario = BuscarForm(request.POST)
	        if formulario.is_valid():
	            #emp = formulario.cleaned_data['empleado']
	            materiales = Materiales.objects.all().filter(material__icontains=formulario.cleaned_data['material'])
	            formulario = BuscarForm()
	    else:
		    #Crea un formulario
		    formulario = BuscarForm()
		    # Obtiene todos los empleados
		    materiales = Materiales.objects.all()
		    # Devuelve los empleados los empleados // OCULTAR DNI
	    return render(request, 'show_materiales.html', {'formulario' : formulario, 'materiales': materiales, 'empleado' : request.session['member_id_nombre']})
	else:
		return redirect('/')

def mod_materiales(request, offset):
    #Comprobamos que haya iniciado sesion, si no se redirige al login
    if 'member_id' in request.session and request.session['member_id_puesto'] == "Desarrollador":
        offset = str(offset)
        material = Materiales.objects.get(etiqueta=offset)
        # si el usuario esta enviando el formulario con datos
        if request.method == 'POST':
            # Aociar datos mandados al formulario
            formulario = FormularioMaterialMod(request.POST)
            if formulario.is_valid():
                material.material = request.POST.get('material')
               	material.trabajador = Empleados.objects.get(dni=request.POST.get('trabajador'))
               	material.save()
                formulario = FormularioMaterialMod()
                return render(request, 'mod_materiales.html', {'formulario' : formulario, 'mat_mod' : 'ok', 'empleado' : request.session['member_id_nombre']})
        else:
            formulario = FormularioMaterialMod(initial={'material' : material.material, 'trabajador' : material.trabajador})
        return render(request, 'mod_materiales.html', {'formulario' : formulario, 'empleado' : request.session['member_id_nombre']})
    else:
        return redirect('/')

def del_materiales(request, offset):
    #Comprobamos que haya iniciado sesion, si no se redirige al login
    if 'member_id' in request.session and request.session['member_id_puesto'] == "Desarrollador":
		offset = str(offset)
		material = Materiales.objects.get(etiqueta=offset)
		# Pedir confirmacion
		material.delete()
		return redirect('/show_materiales/')
		#return	render(request, 'show_empleados.html', {'emp_del' : 'ok'})
    else:
        return redirect('/')