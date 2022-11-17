import os
from pathlib import Path
from re import LOCALE

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+!8kxy9a($_bm!aj!+y0b-q-s+$7nc!w0c2#0@c1714a_oww_w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['asociacionusar.herokuapp.com', '*']
#ALLOWED_HOSTS = ['*']

 
# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aplicacion',
]

#LOCALE_PATHS=[os.path.join(BASE_DIR,"")]

"""
JAZZMIN_SETTINGS={
    'site_header': 'Usar Administrador'
}
"""

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sistema.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sistema.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

"""
#BASE DE DATOS MySQL
DATABASES = {
    #Cambiamos el nombre de nuestra base de datos que sera mysql
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #Nombre de nuestra base de datos
        'NAME': 'mascotas',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
"""
#----------------------------------------------------
"""
#BASE DE DATOS POSTGRESQL
DATABASES = {
    #Cambiamos el nombre de nuestra base de datos que sera mysql
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #Nombre de nuestra base de datos
        'NAME': 'daj4bn0q6j3m50',
        'USER': 'jqveyjfrjzkgyi',
        'PASSWORD': 'dadedcf2926a73e421c5603dacb6b87e9d060d74fa90cc4ea97a9ccd1da905dd',
        'HOST': 'ec2-44-205-177-160.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}
"""
#-----------------------------------------
"""
#BASE DE DATOS SQLITE3
DATABASES = {
    #Base de datos default(sqlite3)
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""
#------------------------------------------

import dj_database_url
from decouple import config

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}


"""
#load_dotenv(find_dotenv())
DATABASES = {'default': dj_database_url.config(default='sqlite:///db.sqlite3', conn_max_age=600)}

#comandos AWS
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_DEFAULT_ACL = config('public-read')

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400'
}

AWS_LOCATION = 'static'
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {
    'Access-Control-Allow-Origin': '*',
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.s3Boto3Storage'

STATICFILES_STORAGE ='storages.backends.s3boto3.s3StaticStorage'
"""

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/imagenes')
#MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
MEDIA_URL = '/imagenes/'

#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#Colocamos la ubicacion del login
LOGIN_REDIRECT_URL = 'inicio'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de email
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST="smtp.gmail.com"
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER='adcomkan7@gmail.com'
EMAIL_HOST_PASSWORD='jpokreiohjpylbie'
