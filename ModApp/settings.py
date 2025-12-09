from pathlib import Path
from django.contrib.messages import constants as messages
from decouple import config  # pour .env
import os
import dj_database_url

# ============================================================
# BASE
# ============================================================
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY", default='django-insecure-ezho_*p@*1$5!c7e^rgv#94jple&^3rjvga7tv=stz+5h(3r+z')

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*", cast=lambda v: [s.strip() for s in v.split(",")])

# ============================================================
# ORANGE MONEY CONFIGURATION
# ============================================================
ORANGE_MONEY_RECEIVER = config("ORANGE_MONEY_RECEIVER")
ORANGE_MONEY_MIN_MONTANT = config("ORANGE_MONEY_MIN_MONTANT", cast=int)
ORANGE_MONEY_API_KEY = config("ORANGE_MONEY_API_KEY")

# ============================================================
# APPLICATIONS
# ============================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'eglise',
    'channels',
    'django_extensions',
]

# ============================================================
# MIDDLEWARE
# ============================================================
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

# ============================================================
# URLS & TEMPLATES
# ============================================================
ROOT_URLCONF = 'ModApp.urls'
WSGI_APPLICATION = 'ModApp.wsgi.application'
ASGI_APPLICATION = 'ModApp.asgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            BASE_DIR / 'eglise' / 'templates',
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

# ============================================================
# DATABASE
# ============================================================
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
    )
}

# ============================================================
# PASSWORD VALIDATION
# ============================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8,}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ============================================================
# INTERNATIONALIZATION
# ============================================================
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Kinshasa'
USE_I18N = True
USE_TZ = True

# ============================================================
# STATIC & MEDIA
# ============================================================
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "eglise" / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ============================================================
# AUTH
# ============================================================
AUTH_USER_MODEL = 'eglise.CustomUser'
LOGIN_URL = 'eglise:connexion'
LOGIN_REDIRECT_URL = 'eglise:accueil'
LOGOUT_REDIRECT_URL = '/'

# ============================================================
# MESSAGES
# ============================================================
MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
}

# ============================================================
# CHANNELS
# ============================================================
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    }
}

# ============================================================
# HTTPS & CORS
# ============================================================
SECURE_SSL_REDIRECT = not DEBUG
CORS_ALLOW_ALL_ORIGINS = True
