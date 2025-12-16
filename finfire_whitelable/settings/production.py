from .base import *

DEBUG = False

# all hosts allowed to run the backend service
ALLOWED_HOSTS = []

# trusted origins for form submission
CSRF_TRUSTED_ORIGINS = [

]

# standard Postgres database setup (no django-tenants)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    }
}

# CORS allowed domains
CORS_ALLOWED_ORIGIN_REGEXES = [
    r'^http[s]{0,1}://[a-zA-Z0-9_-]+\.finfireapplication\.com',
    r'^http[s]{0,1}://finfireapplication\.com',
]



ALLOWED_FRONTEND_ORIGINS = [
    
]

