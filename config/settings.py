# For more information on this file, see
# https://docs.djangoproject.com/en/2.0/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/2.0/ref/settings/

import os
import sys
from django.utils.translation import ugettext_lazy as _

# from .local import settings_local
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Path directory description
PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(PROJECT_DIR)

VENDOR_DIR = os.path.join(BASE_DIR, 'vendor')
APPS_DIR = os.path.join(BASE_DIR, 'apps')

if VENDOR_DIR not in sys.path:
    sys.path.insert(0, VENDOR_DIR)
if APPS_DIR not in sys.path:
    sys.path.insert(0, APPS_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#!jp&=h2+lzkpd)tsb8)zh#afp^ky-((=e*7z@f(4##+-d1i-0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['lab.ajipratama.net', '127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'suit',
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps
    'news',

    # Vendor
    'tastypie',

]

# SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Auth User Models
# AUTH_USER_MODEL = 'account.User'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


# For Postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'newsapp',
        'USER': 'newsapp',
        'PASSWORD': ''
    }
}

# For Sqlite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


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

LANGUAGE_CODE = 'id'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('id', _('Bahasa Indonesia')),
    ('en', _('English')),
]

# ADMIN_READONLY_GROUP = 'READONLY'
# ADMIN_RESTRICT_ADD_GROUP = 'RESTRICT_ADD'
# ADMIN_RESTRICT_DELETE_GROUP = 'RESTRICT_DELETE'

# modeltranslation configuration entry
MODELTRANSLATION_LANGUAGES = ('id', 'en')
MODELTRANSLATION_DEFAULT_LANGUAGE = 'id'
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'id'
MODELTRANSLATION_FALLBACK_LANGUAGES = ('id', 'en')

# if not LIVEHOST:
#     MODELTRANSLATION_DEBUG = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# Tastypie
TASTYPIE_DEFAULT_FORMATS = ['json']
