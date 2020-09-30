import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#ROOT_DIR = os.path.dirname(BASE_DIR)
SECRET_KEY = 'wa!^ehdwzn6!_@udp%3dz@u906o3p_-%qgq(esvq-8y2utsjmw'

# SECURITY WARNING: don't run with debug turned on in production!
SITE_ID = 1
DEBUG = True
PAGINATE_BY = 10
TAGS_PAGINATE_BY = 500
ADMIN_LIST_PER_PAGE = 20
ALLOWED_HOSTS = ['*']

# Email Settings
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'comelizer@gmail.com'
EMAIL_HOST_PASSWORD = 'x'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
FILE_UPLOAD_MAX_MEMORY_SIZE = 35000000

# Production mode
if not DEBUG:
    # activate the logging

    # from djangoblog.utils.logger import LOGGING
    # LOGGING = LOGGING

    # to enable / disable `HTML Minify` middleware
    HTML_MINIFY = True

    # to enable send an email for logging errors
    SERVER_EMAIL = EMAIL_HOST_USER
    ADMINS = [('Abimanyu Yusuf', EMAIL_HOST_USER), ]
    MANAGERS = ADMINS

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'django.contrib.sitemaps',
    'django.contrib.sites',

    # 3d party apps
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',

    # major apps
    'apps.core',
    'apps.profil',
    'apps.berita',
    'apps.qapuas'
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

ROOT_URLCONF = 'sidpy.urls'

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
                
                'apps.profil.context_processors.menu_pages',
                'apps.profil.context_processors.menu_pages_category',
                'apps.profil.context_processors.menu_pages_ppid',

                'apps.berita.context_processors.menu_category',
                'apps.qapuas.context_processors.Qconf',
            ],
        },
    },
]

WSGI_APPLICATION = 'sidpy.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sidpy_0_1',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
"""

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "CDN") # CDN or public_html/CDN
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'assets/media') # Development
# MEDIA_ROOT = os.path.join(BASE_DIR, 'CDN/media') # Production
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
CKEDITOR_UPLOAD_PATH = 'images/'