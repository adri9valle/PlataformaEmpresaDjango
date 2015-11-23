from django.template import RequestContext
from django.shortcuts import render, redirect
from forms import FormularioLogin
from gestion_empleados.models import Empleados, CalendarioLaboral
from gestion_departamentos.models import Puestos
# Importamos ObjectDoesNotExist para las excepciones:
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
import time, datetime

def login(request):
    #if request.session['member_id']:
    if 'member_id' in request.session:
        return redirect('/show_perfil/')
        #return HttpResponse("Ya estas logueado tio")
    else:
        fecha = time.strftime("%d/%m/%y")
        mensaje = ''
        if request.method == 'POST':
            formulario = FormularioLogin(request.POST)
            if formulario.is_valid():
                #Si el formulario es valido hace una consulta con los valores recibidos del formulario
                try:
                    #Comprueba que el usuario existe:
                    e = Empleados.objects.get(dni__exact=formulario.cleaned_data['user'])
                    if e.dni == formulario.cleaned_data['passwd']:
                        request.session['member_id'] = e.dni
                        request.session['member_id_nombre'] = e.nombre
                        request.session['member_id_puesto'] = e.puesto.puesto
                        #print request.session['member_id_puesto']
                        #mensaje = 'Estas logueado'
                        dia_trabajado(request.session['member_id'])
                        return redirect('/show_perfil/')
                    else:
                        mensaje = "Clave incorrecta"
                #Si hay error en la consulta:
                except ObjectDoesNotExist:
                    mensaje = "Usuario no existe"
        else:
            formulario = FormularioLogin()
        return render(request, 'index.html', {'formulario': formulario, 'fecha': fecha, 'mensaje' : mensaje})

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    #return HttpResponse("Estas deslogueado.")
    return redirect('/')
    
def dia_trabajado(dni):
    empleado = Empleados.objects.get(dni=dni)
    fecha = time.strftime("%Y-%m-%d")
    try:
        c = CalendarioLaboral.objects.get(fecha=fecha,trabajador=empleado)
    except ObjectDoesNotExist:
        c = CalendarioLaboral(trabajador=empleado)
        c.save()