
"""#Importes necesarios para el funcionamiento de la app
from pathlib import Path
#import environ
import os

#SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
#SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

#Lectura de variables de entorno
#env = environ.Env()
# reading .env file
#environ.Env.read_env()


#Configuracion de Mensajeria 
#TWILIO_ACCOUNT_SID   = env('TWILIO_ACCOUNT_SID',default=False, cast=str)
#TWILIO_AUTH_TOKEN    = env('TWILIO_AUTH_TOKEN',default=False, cast=str)
#TWILIO_PHONE_NUMBER  = env('TWILIO_PHONE_NUMBER',default=False, cast=str)


# Configuración para enviar correos a través del servidor SMTP de Google
#EMAIL_BACKEND       = env('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend', cast=str)
#EMAIL_HOST          = env('EMAIL_HOST', default='smtp.gmail.com', cast=str)
#EMAIL_PORT          = env('EMAIL_PORT', default=587, cast=int)
#EMAIL_USE_TLS       = env('EMAIL_USE_TLS', default=True, cast=bool)
#EMAIL_HOST_USER     = env('EMAIL_HOST_USER', default=False, cast=str)
#EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default=False, cast=str)



BASE_DIR = Path(__file__).resolve().parent.parent
print("SECRET_KEY desde os.environ:", os.getenv('SECRET_KEY'))

#SECRET_KEY = env('SECRET_KEY')

# Configuraciones adicionales
#DEBUG = env.bool("DEBUG", default=False)
#ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = env('DEBUG', default=False)

ALLOWED_HOSTS = ALLOWED_HOSTS=[   
    'xilenadesigns.pythonanywhere.com',
    '127.0.0.1',
    'localhost',
    ]

LOGIN_REDIRECT_URL = 'adminHome'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Dependencias instaladas
    'django.contrib.humanize',
    #Apps Propias
    'Products',
    'Admin',
    'Users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'XilenaDesigns.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            #Ruta a las carpetas templates
            os.path.join(BASE_DIR, 'Products', 'productTemplates'),  # Ruta a la carpeta productsTemplates,
            os.path.join(BASE_DIR, 'Admin', 'adminTemplates'),  # Ruta a la carpeta productsTemplates,
            os.path.join(BASE_DIR, 'templates'),  # Ruta a la carpeta productsTemplates,
        ],
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

WSGI_APPLICATION = 'XilenaDesigns.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE   = 'en-us'

TIME_ZONE       = 'UTC'

USE_I18N        = True

USE_TZ          = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
#Ruta a las carpetas static
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'Products', 'productStatic'),  # Ruta a la carpeta static,
    os.path.join(BASE_DIR, 'Admin', 'adminStatic'),  # Ruta a la carpeta static,
    os.path.join(BASE_DIR ,'static'),  # Ruta a la carpeta static,
    #añadir la ruta a la carpeta static de Admin
]


#configuracion de archivos multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,"media")


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD    = 'django.db.models.BigAutoField'



"""

"""
Django settings for commercializadora project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ykw2d5%e_xuy720-ndkxka6&6a66mnd2u4x(fug6l2_^-49$0l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Products',
    'Admin',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'XilenaDesigns.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            #Ruta a las carpetas templates
            os.path.join(BASE_DIR, 'Products', 'productTemplates'),  # Ruta a la carpeta productsTemplates,
            os.path.join(BASE_DIR, 'Admin', 'adminTemplates'),  # Ruta a la carpeta productsTemplates,
            os.path.join(BASE_DIR, 'templates'),  # Ruta a la carpeta productsTemplates,
        ],
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
WSGI_APPLICATION = 'XilenaDesigns.wsgi.application'



# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
#Ruta a las carpetas static
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'Products', 'productStatic'),  # Ruta a la carpeta static,
    os.path.join(BASE_DIR, 'Admin', 'adminStatic'),  # Ruta a la carpeta static,
    os.path.join(BASE_DIR ,'static'),  # Ruta a la carpeta static,
    #añadir la ruta a la carpeta static de Admin
]

# Configuración de archivos de medios
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


#STATIC_URL = 'static/'
#MEDIA_URL='/Media/'
#MEDIA_ROOT=os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
