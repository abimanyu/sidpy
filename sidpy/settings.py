import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
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

# Martor (Markdown Editor)
MARTOR_THEME = 'bootstrap'
MARTOR_ENABLE_CONFIGS = {
    'imgur': 'true',        # to enable/disable imgur/custom uploader.
    'jquery': 'true',       # to include/revoke jquery (require for admin default django)
    'hljs': 'true',         # to enable/disable hljs highlighting in preview
}
# To show the toolbar buttons
MARTOR_TOOLBAR_BUTTONS = [
    'bold', 'italic', 'horizontal', 'heading', 'pre-code',
    'blockquote', 'unordered-list', 'ordered-list',
    'link', 'image-link', 'image-upload',
    'direct-mention', 'toggle-maximize', 'help'
]
# To setup the martor editor with title label or not (default is False)
MARTOR_ENABLE_LABEL = False
# Markdownify
MARTOR_MARKDOWNIFY_FUNCTION = 'martor.utils.markdownify' # default
MARTOR_MARKDOWNIFY_URL = '/martor/markdownify/' # default
# Markdown extensions (default)
MARTOR_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.nl2br',
    'markdown.extensions.smarty',
    'markdown.extensions.fenced_code',
    # Custom markdown extensions.
    'martor.extensions.urlize',
    'martor.extensions.del_ins',      # ~~strikethrough~~ and ++underscores++
    'martor.extensions.mention',      # to parse markdown mention
    'martor.extensions.emoji',        # to parse markdown emoji
    'martor.extensions.mdx_video',    # to parse embed/iframe video
    'martor.extensions.escape_html',  # to handle the XSS vulnerabilities
]
# Markdown Extensions Configs
MARTOR_MARKDOWN_EXTENSION_CONFIGS = {}
# Markdown urls
MARTOR_UPLOAD_URL = '/martor/uploader/' # default
MARTOR_SEARCH_USERS_URL = '/martor/search-user/' # default

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
    'martor', # markdown

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
                'apps.profil.context_processors.menu_profil',
                'apps.profil.context_processors.menu_kategori',
                'apps.berita.context_processors.menu_category',
                'apps.profil.context_processors.menu_profil_ppid',
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
        'NAME': 'DB_NAME',
        'USER': 'DB_USER',
        'PASSWORD': 'DB_PASSWORD',
        'HOST': 'localhost',
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
    os.path.join(BASE_DIR, "static"),
]
STATIC_URL = '/static/'