import os
from os.path import dirname, join
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_path = join(dirname(__file__), '../dev.env')
load_dotenv(dotenv_path)

DEBUG = os.environ.get('DEBUG', default='True') == 'True'
SECRET_KEY = os.environ.get('SECRET_KEY')

ENGINE = os.environ.get('ENGINE')
NAME = os.environ.get('NAME')
USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')
HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')

DOMEN = os.environ.get('DOMEN')


ALLOWED_HOSTS = ['*'] if DEBUG else [DOMEN, f'www.{DOMEN}']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'homepage',
    'product',
    'core',

    'sorl.thumbnail',
    'django_cleanup.apps.CleanupConfig',
    'meta',
    'froala_editor',
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


ROOT_URLCONF = 'Keratech.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
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


WSGI_APPLICATION = 'Keratech.wsgi.application'


DATABASES = {
    'default': {
       'ENGINE': ENGINE,
       'NAME': NAME,
       'USER': USER,
       'PASSWORD': PASSWORD,
       'HOST': HOST,
       'PORT': PORT,
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static_dev',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


FROALA_EDITOR_OPTIONS = {
    'quickInsertEnabled': False,
    'language': 'ru',
    'toolbarButtons': [
        'bold', 'italic', 'underline', 'strikeThrough',
        'fontSize', 'color',
        'paragraphFormat', 'align',
        'formatOL', 'formatUL',
        'insertTable',
        'undo', 'redo',
    ],
    'height': 500,
    'width': 500,
    'charCounterCount': True,
    'toolbarInline': False,
}


CSRF_COOKIE_HTTPONLY = False

META_USE_TITLE_TAG = True
META_USE_SCHEMAORG_PROPERTIES = True
META_USE_OG_PROPERTIES = True
META_DEFAULT_IMAGE = 'https://keratekh.ru/static/favicon/logo_text.svg'
META_SITE_PROTOCOL = 'http' if DEBUG else 'https'
META_SITE_DOMAIN = DOMEN
