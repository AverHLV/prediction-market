"""
Django settings for market project.

Generated by 'django-admin startproject' using Django 2.0.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

from django.utils.translation import ugettext_lazy as _

from os import environ
from pathlib import Path
from configparser import ConfigParser

from utils import OpenWeatherMap

BASE_DIR = Path.cwd()

config = ConfigParser()
config.read(BASE_DIR / 'config' / (environ['MARKET_CONF'] if 'MARKET_CONF' in environ else 'default.ini'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

SECRET_KEY = config.get('django', 'secret_key')

DEBUG = True if config.get('django', 'debug') == 'true' else False

ALLOWED_HOSTS = [host for host in config.get('django', 'hosts').split()]

ROOT_URLCONF = 'config.urls'
AUTH_USER_MODEL = 'markets.MarketUser'

SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'username'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'rest_framework',
    'rest_framework.authtoken',

    # another packages

    'django_celery_beat',
    'rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth.registration',
    'corsheaders',
    'channels',

    # own apps

    'markets',
]

# Logging configuration

if not DEBUG:
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
                'maxBytes': 104857600,
            },
        },

        'loggers': {
            'django': {
                'handlers': ['file_handler'],
                'level': 'INFO',
                'propagate': True,
            },

            'custom': {
                'handlers': ['file_handler'],
                'level': 'INFO',
                'propagate': True,
            }
        }
    }

# REST API settings

API_VERSION = 'v1'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),

    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}

if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('rest_framework.renderers.BrowsableAPIRenderer')

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'markets.serializers.UserSerializer',
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'build',
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

FIXTURE_DIRS = [
    BASE_DIR / 'fixtures',
]

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.routing.application'

if DEBUG:
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            'CONFIG': {
                "hosts": [(config.get('redis', 'redis_host'), config.get('redis', 'redis_port'))],
            },
        },
    }
else:
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            'CONFIG': {
                "hosts": [config.get('redis', 'redis_host')],
            },
        },
    }

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [config.get('redis', 'redis_host')],
#         },
#     },
# }

# Third party APIs

OWM_CLIENT = OpenWeatherMap(config.get('keys', 'owm_id'))

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config.get('database', 'db_name'),
        'USER': config.get('database', 'db_user'),
        'PASSWORD': config.get('database', 'db_pass'),
        'HOST': config.get('database', 'db_host'),
        'PORT': config.get('database', 'db_port'),
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

LOCALE_PATHS = (
    BASE_DIR / 'locale',
)

LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russian')),
    ('uk', _('Ukrainian')),
)

LANGUAGE_CODE = LANGUAGES[0][0]

TIME_ZONE = 'Europe/Kiev'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Celery settings

timezone = TIME_ZONE
task_ignore_result = True
app_name = config.get('celery', 'app_name')
broker_url = config.get('celery', 'broker_url')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = [
    BASE_DIR / 'build' / 'static',
    BASE_DIR / 'build',
]

CSRF_COOKIE_NAME = "csrftoken"

CORS_ORIGIN_ALLOW_ALL = True


