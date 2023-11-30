from pathlib import Path
import os
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rqvk484(-p9+z_6-^@zh4jola3#$*x$=+pu3!53xi(63euwu5s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
  "CLOUD_NAME" : "dhrexohux", 
  "API_KEY" : "232777867795216", 
  "API_SECRET" : "a71Ac7OYmW_162esgquS8AIvRZg"
}


CORS_ORIGIN_WHITELIST = ["*.onrender.com","*","ehelath237.onrender.com","*onrender.com"]


ALLOWED_HOSTS = ["*"]

DJOSER = {
    'SERIALIZERS': {
        'user': 'chat.serializers.CustomUserSerializer',
        # Include other custom serializers if you have any
    },
}




MEDIA_URL = '/cloud-assignment/media/'

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

# Application definition

INSTALLED_APPS = [
    'jet',
    'jet.dashboard',
    'daphne',
    'corsheaders',
    'djoser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'listings',
    'chat'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ehealth.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'ehealth.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cloud',
        'USER': 'asbilim',
        'PASSWORD': 'saR16gXqELPZ',
        'HOST': 'ep-super-snow-812319.us-east-2.aws.neon.tech',
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'require'},
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'listings.People'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# channel configuration


ASGI_APPLICATION = 'ehealth.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        # "BACKEND": "channels_redis.core.RedisChannelLayer",
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
        # "CONFIG": {
        #     "hosts": [("127.0.0.1", 6379)],
        # },
    },
}


# end channel configuration

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",

]

CORS_ALLOW_ALL_ORIGINS = True



#image configuration

ALLOWED_HOSTS = ['*']

MEDIA_URL = '/lachofit/media/'

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')


#djoser


REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )

}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7)
}


