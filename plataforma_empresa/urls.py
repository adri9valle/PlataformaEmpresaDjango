from django.conf.urls import patterns, include, url

#Importamos settings para que coja la static  con los archivos css
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

#Importamos nuestras funciones
from views import login, logout
from gestion_empleados.views import add_empleado, show_empleados, mod_empleados, del_empleados, show_perfil, cargar_empleados, exportar_empleados, calendario_laboral
from gestion_materiales.views import add_material, show_materiales, mod_materiales, del_materiales
from gestion_departamentos.views import add_departamento, add_puesto, show_departamentos, show_puestos, del_departamentos, del_puestos
from gestion_incidencias.views import add_incidencia, show_incidencias, del_incidencias

urlpatterns = patterns('',

    url(r'^$', login),
    url(r'^logout/$', logout),

    #Sitio Administracion
    url(r'^admin/', include(admin.site.urls)),

    
    url(r'^add_material/$', add_material),
    url(r'^show_materiales/$', show_materiales),
    url(r'^mod_materiales/(\S+)/$', mod_materiales),
    url(r'^del_materiales/(\S+)/$', del_materiales),
        
    url(r'^add_departamento/$', add_departamento),
    url(r'^show_departamentos/$', show_departamentos),
    url(r'^del_departamentos/(\S+)/$', del_departamentos),
    
    url(r'^add_puesto/$', add_puesto),
    url(r'^show_puestos/$', show_puestos),
    url(r'^del_puestos/(\S+)/$', del_puestos),
    
    url(r'^add_incidencia/$', add_incidencia),
    url(r'^show_incidencias/$', show_incidencias),
    url(r'^del_incidencias/(\d+)/$', del_incidencias),
    
    url(r'^add_empleado/$', add_empleado),
    url(r'^show_empleados/$', show_empleados),
    url(r'^cargar_empleados/$', cargar_empleados),
    url(r'^exportar_empleados/$', exportar_empleados),
    url(r'^mod_empleados/(\S+)/$', mod_empleados),
    url(r'^del_empleados/(\S+)/$', del_empleados),
    url(r'^calendario_laboral/$', calendario_laboral),
    
    url(r'^show_perfil/$', show_perfil),
)

