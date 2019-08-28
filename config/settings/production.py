"""
Django settings for market project.

Generated by 'django-admin startproject' using Django 2.0.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

from unipath import Path
from utils import secret_dict

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_dict['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Logging configuration

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'simple_formatter': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },

    'handlers': {
        'file_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'main.log',
            'formatter': 'simple_formatter',
            'maxBytes': 104857600
        },
    },

    'loggers': {
        'django': {
            'handlers': ['file_handler'],
            'level': 'INFO',
            'propagate': True
        },

        'custom': {
            'handlers': ['file_handler'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

# Admins contacts
ADMINS = [(admin['name'], admin['email']) for admin in secret_dict['admins']]

# Hosts
ALLOWED_HOSTS = secret_dict['hosts']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'config.urls'

BASE_DIR = Path(__file__).ancestor(3)
BASE_NAME = BASE_DIR[BASE_DIR.rfind('\\') + 1:]
STATIC_ROOT = BASE_DIR.child('static')
STATIC_VERSION = '1.0.0'

STATICFILES_DIRS = (
    BASE_DIR.child('assets'),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.child('templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': secret_dict['db_name'],
        'USER': secret_dict['db_admin'],
        'PASSWORD': secret_dict['db_pass'],
        'HOST': secret_dict['db_host'],
        'PORT': secret_dict['db_port'],
        'ATOMIC_REQUESTS': True
    }
}

# Security settings
SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Celery settings

timezone = TIME_ZONE
task_ignore_result = True
broker_url = secret_dict['broker_url']

if not len(broker_url):
    broker_url = None

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
