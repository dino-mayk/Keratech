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
    'about',
    'core',

    'sorl.thumbnail',
    'django_cleanup.apps.CleanupConfig',
    'meta',
    'imagekit',
    'ckeditor',
    'ckeditor_uploader',
    'colorful',
    'adminsortable',
    'djeym',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.middleware.locale.LocaleMiddleware',
    'djeym.middlewares.AjaxMiddleware',
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


CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_FILENAME_GENERATOR = 'djeym.utils.get_filename'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_CONFIGS = {
    'default': {
        'language': 'ru',
        'toolbar': [
            {
                'name': 'basicstyles', 'items': [
                    'Bold',
                    'Italic',
                    'Underline',
                    'Strike',
                ]
            },
            {
                'name': 'paragraph',
                'items': [
                    'Format',
                    'JustifyLeft',
                    'JustifyCenter',
                    'JustifyRight',
                    'JustifyBlock',
                ]
            },
            {
                'name': 'list',
                'items': [
                    'NumberedList',
                    'BulletedList',
                ]
            },
            {
                'name': 'links',
                'items': [
                    'Undo',
                    'Redo',
                ]
            },
            {
                'name': 'insert',
                'items': [
                    'Table',
                ]
            },
            {
                'name': 'styles',
                'items': [
                    'FontSize',
                    'TextColor',
                ]
            },
        ],
        'height': 500,
        'width': 500,
        'allowedContent': True,
        'extraPlugins': ','.join([
            'uploadimage',
            'div',
            'autolink',
            'autogrow',
        ]),
        'removePlugins': 'stylesheetparser',
        'charCounterCount': True,
        'forcePasteAsPlainText': True,
    },
    'djeym': {
        'toolbar': 'full',
        'height': 400,
        'width': 362,
        'colorButton_colors': 'FFFFFF,F08080,CD5C5C,FF0000,FF1493,C71585,'
                              '800080,F0E68C,BDB76B,6A5ACD,483D8B,3CB371,'
                              '008000,808000,2E8B57,9ACD32,20B2AA,008B8B,'
                              '00BFFF,F4A460,CD853F,A52A2A,708090,34495e,'
                              '999966,333333,82cdff,1e98ff,177bc9,0e4779,'
                              '97a100,595959,b3b3b3,f371d1,b51eff,793d0e,'
                              'ffd21e,ff931e,56db40,1bad03,e6761b,ed4543',
        'colorButton_enableAutomatic': False,
        'colorButton_enableMore': True
    }
}

LOGIN_URL = '/admin/'

JQUERY_URL = False
USE_DJANGO_JQUERY = True

DJEYM_YMAPS_API_KEY = ''

DJEYM_YMAPS_ICONS_FOR_CATEGORIES_CSS = []
DJEYM_YMAPS_ICONS_FOR_CATEGORIES_JS = []


CSRF_COOKIE_HTTPONLY = False

META_USE_TITLE_TAG = True
META_USE_SCHEMAORG_PROPERTIES = True
META_USE_OG_PROPERTIES = True
META_DEFAULT_IMAGE = 'https://keratekh.ru/static/favicon/logo_text.svg'
META_SITE_PROTOCOL = 'http' if DEBUG else 'https'
META_SITE_DOMAIN = DOMEN
