from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [

    'http://localhost:8000',
]

# postgres database setup — tenants enabled
DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    }
}

# CORS_ALLOWED_ORIGIN_REGEXES = [
#     r'^http[s]{0,1}://localhost:\d{2,5}$',
#     r'^http[s]{0,1}://[a-zA-Z0-9_-]+\.localhost:\d{2,5}$',
#     r'^http[s]?://[a-zA-Z0-9_-]+\.localhost(?::\d{2,5})?$',

#     r'^http[s]{0,1}://[a-zA-Z0-9_-]+\.dev\.renon\.ai',
#     r'^http[s]{0,1}://[a-zA-Z0-9_-]+\.renon\.ai',
#     r'^http[s]{0,1}://[a-zA-Z0-9_-]+\.staging\.renon\.ai',
# ]


CORS_ALLOW_ALL_ORIGINS=True


ALLOWED_FRONTEND_ORIGINS = [
    

]



