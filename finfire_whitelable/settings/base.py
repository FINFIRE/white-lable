from pathlib import Path
import os
import environ
from pathlib import Path
from datetime import timedelta

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = []

# Application definition



SHARED_APPS = (
    'django_tenants',
    'tenants.apps.TenantsConfig',
    'django.contrib.contenttypes',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_filters',
    'django_extensions',
    'debug_toolbar',
    'drf_yasg',
    'drf_spectacular',
    'djoser',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',


    'Algorithm.apps.AlgorithmConfig',

)


TENANT_APPS = (
    'django.contrib.contenttypes',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'registration.apps.RegistrationConfig',
    'iquestions.apps.IquestionsConfig',
    'CM_Market.apps.CmMarketConfig',
    'entreprise_questions.apps.EntrepriseQuestionsConfig',
    'connections.apps.ConnectionsConfig',
    'master_review.apps.MasterReviewConfig',
    'Matching_Algorithm.apps.MatchingAlgorithmConfig',
    'truth_in_capital.apps.TruthInCapitalConfig',

    # authtoken belongs to each tenant schema so DRF tokens FK to that
    # tenant's auth_user. Listed in SHARED_APPS too (mirroring auth /
    # token_blacklist) so the public schema also has its own table for
    # platform-admin flows.
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',

    'djoser',

)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]



MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'finfire_whitelable.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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


WSGI_APPLICATION = 'finfire_whitelable.wsgi.application'


REST_FRAMEWORK = {
    "COERCE_DECIMAL_TO_STRING": False,
    "NON_FIELD_ERROR_KEY": "error",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.FormParser",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.MultiPartRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.UserRateThrottle",
    ],
    # 'EXCEPTION_HANDLER': 'utils.error_handler.custom_exception_handler',
}

SPECTACULAR_SETTINGS = {
    "TITLE": "FINFIRE API",
    "DESCRIPTION": "FINFIRE api doc for front end.",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}


# Rest framework jwt validation token lifetime
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=2),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True
}


DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'resetPasswordConfirm/{uid}/{token}',
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'ACTIVATION_URL': 'userActivate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'EMAIL': {
        'activation': 'finfire_whitelable.djoser_overrides.CustomActivationEmail',
        'password_reset': 'finfire_whitelable.djoser_overrides.CustomPasswordResetEmail',
    },
    'SERIALIZERS': {
        'user': 'finfire_whitelable.djoser_overrides.CustomUserSerializer',
        'current_user': 'finfire_whitelable.djoser_overrides.CustomUserSerializer',
        'user_create': 'finfire_whitelable.djoser_overrides.CustomUserCreateSerializer',
        'user_create_password_retype': 'finfire_whitelable.djoser_overrides.CustomUserCreatePasswordRetypeSerializer',
    },
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


# Email setup
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")



# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = ['127.0.0.1']

# Webhook (per-tenant override possible via env)
PAYLOAD_WEBHOOK_URL = env('PAYLOAD_WEBHOOK_URL', default='https://hook.us2.make.com/hn4fn71gzd7kvamax4ye5hissivcizz2')
PAYLOAD_WEBHOOK_TIMEOUT = env.int('PAYLOAD_WEBHOOK_TIMEOUT', default=30)
PAYLOAD_WEBHOOK_RETRY_ATTEMPTS = env.int('PAYLOAD_WEBHOOK_RETRY_ATTEMPTS', default=3)

TENANT_MODEL = "tenants.Client" # app.Model

TENANT_DOMAIN_MODEL = "tenants.Domain"  # app.Model



# urls config for global and tenant urls
ROOT_URLCONF = 'finfire_whitelable.urls'
PUBLIC_SCHEMA_URLCONF = 'finfire_whitelable.public_urls'
SHOW_PUBLIC_IF_NO_TENANT_FOUND = True



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[{asctime}] [{levelname}] {name}: {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'django_file': {
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/django.log',
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'django_file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}



