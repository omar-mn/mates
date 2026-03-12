import dj_database_url
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gpooiwq9+a@xg)wm0zop%jf4iyncv(prcm5@a@cw^&sb62^#3h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'corsheaders',

    # apps
    'Rooms',
    'Users',
    'Messages',
    'channels',


    # dj-rest-auth
    'rest_framework',
    'rest_framework.authtoken', 
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'Mates.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'Mates.wsgi.application'
ASGI_APPLICATION = 'Mates.asgi.application'

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "b2gj6jiyrj3q5lqg885e",
#         "USER": "u5fbl3kt0xxuspa5jeod",
#         "PASSWORD": "2i4lNjYcQYrpy7JhBKKuaFc4l1BpF0",
#         "HOST": "b2gj6jiyrj3q5lqg885e-postgresql.services.clever-cloud.com",
#         "PORT": "50013",
#     }
# }

DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        ssl_require=True
    )
}


#custom user model

AUTH_USER_MODEL = 'Users.account'


#SIMPLE JWT AUTH

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# SIMPLE_JWT = {
#     'ALGORITHM': 'HS256', 
#     'SIGNING_KEY': 'SECRET_KEY', 
#     # 'AUDIENCE': None,
#     # 'ISSUER': None,
#     # 'JWK_URL': None,
#     # 'LEEWAY': 0,
# }

#CORS

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3030',
    'http://localhost:5173',
]


# AUTH

REST_AUTH = {
    'USER_DETAILS_SERIALIZER': 'Users.serializers.UserInfo',
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'jwt-auth',
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_AUTHENTICATION_METHOD = 'email'  
ACCOUNT_EMAIL_REQUIRED = True           
ACCOUNT_UNIQUE_EMAIL = True
SITE_ID = 2

# EMAIL


# CHANNELS

CHANNEL_LAYERS = {
    'defualt': {
        'BACKEND':'channels.layers,InMemoryChannelLayer'
    }
}

# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]

MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR , 'media')