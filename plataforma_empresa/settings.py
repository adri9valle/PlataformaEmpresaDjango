"""
Django settings for plataforma_empresa project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1p^c=stsmo=%442#@#$qbtxh01yu7wc)@d0@e5nvgxcj32va5!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestion_empleados',
    'gestion_materiales',
    'gestion_departamentos',
    'gestion_incidencias',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'plataforma_empresa.urls'

WSGI_APPLICATION = 'plataforma_empresa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'PLATAFORMA_EMPRESA',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '',
        'PORT': '',
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


# NECESARIO PARA ARCHIVOS ESTATICOS(SE USARA PARA CSS,JS,etc)
STATIC_URL = '/static/'

STATICFILES_DIRS = (
os.path.join(BASE_DIR, "static"),
'/static',
)

#Ruta de las plantillas HTML
TEMPLATE_DIRS = ('templates/',)

# Archivos almacenados
MEDIA_ROOT = '/media/Datos/2ASIR/PROYECTO_FINAL/DJANGO/plataforma_empresa/media/'
MEDIA_URL = '/media/'