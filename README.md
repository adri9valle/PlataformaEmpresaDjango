# PlataformaEmpresaDjango

Requisitos:
  - Django 1.6.1
  - Bootstrap(ya incluido en el proyecto)
  - Python2.7

La instalación de Django se puede realizar mediante el comando pip:
  
  -sudo pip install django==1.6.1
  
Si se usan otra versión de Django podría dar problemas de incompatibilidad con el código actual. 

Para sincronizar los modelos con la base de datos debemos configurar el tipo de conexión de la base de datos en el archivo plataforma_empresa/settings.py y una vez configurado ejecutar:

 -python manage.py syncdb
 
Por último para ver la plataforma en funcionamiento la inicializamos con:
 
  -python manage.py runserver
  
  De este modo sólo atenderá las peticiones locales, para que escuche todas:
  
  -python manage.py runserver 0.0.0.0:(puerto deseado)
  -python manage.py runserver 0.0.0.0:80
  
Con esto ya estará lista.
  
