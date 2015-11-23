from django.shortcuts import render, redirect
#from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.db import connection

from .models import Empleados, ArchivoCarga, CalendarioLaboral
from .forms import FormularioEmpleado, FormularioEmpleadoMod, BuscarEmpleadoForm, SubirArchivoForm, CalendarioForm

from gestion_departamentos.models import Puestos
from gestion_materiales.models import Materiales

import csv, os, time
# Create your views here.

def add_empleado(request):
    #Comprobamos que haya iniciado sesion, si no se redirige al login
    if 'member_id' in request.session and request.session['member_id_puesto'] == "Desarrollador":
    	# Si el usuario esta enviando el formulario con datos
    	if request.method == 'POST': 
    		# Asociar datos al formulario
    		formulario = FormularioEmpleado(request.POST) 
    		# Si los datos son validos
    		if formulario.is_valid():
    			# Guardar los datos en la base de datos
    	   		formulario.save() 
    	   		# Devuelve una vez guardado el formulario vacio para seguir anadiendo empleados
    	   		formulario = FormularioEmpleado()
    	   		return render(request, 'add_empleado.html', {'formulario' : formulario, 'emp_saved' : 'ok', 'empleado' : request.session['member_id_nombre']})
    	# Si el usuario no ha enviado datos(esta llamando a la url add_empleado)
    	else:
    		# Crea un formulario vacio
    	    formulario = FormularioEmpleado()
    	# Devuelve el formulario vacio para anadir empleados
    	return render(request, 'add_empleado.html', {'formulario': formulario, 'empleado' : request.session['member_id_nombre']})
    else:
        return redirect('/')

def show_empleados(request):
    #Comprobamos que haya iniciado sesion, si no se redirige al login
    if 'member_id' in request.session and request.session['member_id_puesto'] == "Desarrollador":
        if request.method == 'POST':
            formulario = BuscarEmpleadoForm(request.POST)
            if formulario.is_valid():
                #emp = formulario.cleaned_data['empleado']
                empleados = Empleados.objects.all().filter(nombre__icontains=formulario.cleaned_data['empleado'])
                formulario = BuscarEmpleadoForm()
        else:
    	    #Crea un formulario
    	    formulario = BuscarEmpleadoForm()
    	    # Obtiene todos los empleados
    	    empleados = Empleados.objects.all()
    	    # Devuelve los empleados los empleados // OCULTAR DNI
        return render(request, 'show_empleados.html', {'formulario' : formulario, 'empleados': empleados, 'empleado' : request.session['member_id_nombre']})
    else:
        return redirect('/')

def mod_empleados(request, offset):
    #Comprobamos que haya iniciado sesion, si no se redirige al login
    if 'member_id' in request.session and request.session['member_id_puesto'] == "Desarrollador":
        offset = str(offset)
        empleado = Empleados.objects.get(dni=offset)
        # si el usuario esta enviando el formulario con datos
        if request.method == 'POST':
            # Aociar datos mandados al formulario
            formulario = FormularioEmpleadoMod(request.POST)
            if formulario.is_valid():
                empleado.apellidos = request.POST.get('apellidos') 
                empleado.telefono = request.POST.get('telefono')
                empleado.direccion = request.POST.get('direccion')
                empleado.correo = request.POST.get('correo')
                empleado.horario = request.POST.get('horario')
                empleado.nombre = request.POST.get('nombre')
                empleado.salario = request.POST.get('salario')
                empleado.puesto =  Puestos.objects.get(puesto=request.POST.get('puesto'))
                empleado.save()
                formulario = FormularioEmpleadoMod()
                return render(request, 'mod_empleados.html', {'formulario' : formulario, 'emp_mod' : 'ok', 'empleado' : request.session['member_id_nombre']})
        else:
            formulario = FormularioEmpleadoMod(initial={'apellidos' : empleado.apellidos, 'telefono' : empleado.telefono, 'nombre' : empleado.nombre, 'direccion' : empleado.direccion, 'correo' : empleado.correo, 'horario' : empleado.horario, 'salario' : empleado.salario, 'puesto' : empleado.puesto})
        return render(request, 'mod_empleados.html', {'formulario' : formulario, 'empleado' : request.session['member_id_nombre']})
    else:
        return redirect('/')

def empleFromCsv(fichero):
    try:
        reader = csv.reader(open('/media/Datos/2ASIR/PROYECTO_FINAL/DJANGO/plataforma_empresa/media/media/%s' % fichero, 'rb'), delimiter=',')
    except ValueError:
        return "Fichero no compatible"
    for row in reader:
        empleado = Empleados()
        empleado.dni = row[0]
        empleado.nombre = row[1]
        empleado.apellidos = row[2]
        empleado.telefono = row[3]
        empleado.direccion = row[4]
        empleado.correo = row[5]
        empleado.horario = row[6]
        empleado.salario = row[7]
        empleado.puesto =  Puestos.objects.get(puesto=(row[8]))
        empleado.save()
    return "Empleados Cargados"        

def cargar_empleados(request):
    if 'member_id' in request.session and request.session['member_id_puesto'] == "Desarrollador":
        if request.method == 'POST':
            formulario = SubirArchivoForm(request.POST, request.FILES)
            if formulario.is_valid():
                formulario.save()
                empleados = empleFromCsv(request.FILES['archivo'])
                print empleados
                archivo = ArchivoCarga.objects.get(archivo='media/%s' % request.FILES['archivo'])
                archivo.delete()
                os.remove('/media/Datos/2ASIR/PROYECTO_FINAL/DJANGO/plataforma_empresa/media/media/%s' % request.FILES['archivo'])
                return redirect('/show_empleados')
        else:
            formulario = SubirArchivoForm()
        return render(request, 'cargar_empleados.html', {'formulario': formulario, 'empleado' : request.session['member_id_nombre']})
    else:
        return redirect('/')

def exportar_empleados(request):
    if 'member_id' in request.session and request.session['member_id_puesto'] == "Desarrollador":
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="empleados.csv"'
        writer = csv.writer(response)
        empleados = Empleados.objects.all()
        for e in empleados:
            writer.writerow([e.dni, e.nombre, e.apellidos, e.telefono, e.direccion, e.correo, e.horario, e.salario, e.puesto])
        return response
    else:
        return redirect('/')       

def del_empleados(request, offset):
    #Comprobamos que haya iniciado sesion, si no se redirige al login
    if 'member_id' in request.session and request.session['member_id_puesto'] == "Desarrollador":
		offset = str(offset)
		empleado = Empleados.objects.get(dni=offset)
		# Pedir confirmacion
		empleado.delete()
		return redirect('/show_empleados/')
		#return	render(request, 'show_empleados.html', {'emp_del' : 'ok'})
    else:
        return redirect('/')

def show_perfil(request):
    if 'member_id' in request.session:
        emp = Empleados.objects.get(dni=request.session['member_id'])
        mat = Materiales.objects.all().filter(trabajador=request.session['member_id'])
        if request.session['member_id_puesto'] != 'Desarrollador':
            return render(request, 'show_perfil_user.html', {'emp' : emp, 'mat' : mat , 'empleado' : request.session['member_id_nombre']})
        else:
            return render(request, 'show_perfil.html', {'emp' : emp, 'mat' : mat , 'empleado' : request.session['member_id_nombre']})
    else:
        return redirect('/')

def calendario_laboral(request):
    if 'member_id' in request.session:
        c = CalendarioLaboral.objects.filter(trabajador=request.session['member_id'])
        if request.method == 'POST':
            formulario = CalendarioForm(request.POST)
            if formulario.is_valid():
                num = request.POST['num']
                opcion = request.POST['opcion']
                if opcion == 'dia':
                    c = CalendarioLaboral.objects.filter(trabajador=request.session['member_id'], fecha__day=num)
                if opcion == 'mes':
                    c = CalendarioLaboral.objects.filter(trabajador=request.session['member_id'], fecha__month=num)
                if opcion == 'ano':
                    c = CalendarioLaboral.objects.filter(trabajador=request.session['member_id'], fecha__year=num)
                if request.session['member_id_puesto'] != 'Desarrollador':
                    return render(request, 'show_calendario_user.html', {'empleado' : request.session['member_id_nombre'], 'calendario' : c, 'formulario' : formulario})
            return render(request, 'show_calendario.html', {'empleado' : request.session['member_id_nombre'], 'calendario' : c, 'formulario' : formulario})
        else:
            formulario = CalendarioForm()
            if request.session['member_id_puesto'] != 'Desarrollador':
                return render(request, 'show_calendario_user.html', {'empleado' : request.session['member_id_nombre'], 'calendario' : c, 'formulario' : formulario})
            else:
                return render(request, 'show_calendario.html', {'empleado' : request.session['member_id_nombre'], 'calendario' : c, 'formulario' : formulario})
    else:
        return redirect('/')
#        INSERT INTO `gestion_empleados_calendariolaboral`(`fecha`, `trabajador_id`, `asistencia`) VALUES ('2014-05-13', '75936191N', True)