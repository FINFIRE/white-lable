from .base import *

DEBUG = False

# all hosts allowed to run the backend service
ALLOWED_HOSTS = []

# trusted origins for form submission. Wildcard host syntax requires
# Django >= 4.0 and matches any subdomain (e.g. acme.appfinfire.com).
CSRF_TRUSTED_ORIGINS = [
    'https://appfinfire.com',
    'https://*.appfinfire.com',
]

# Postgres database setup — django-tenants backend so the middleware can
# switch search_path per request based on the resolved tenant.
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

# Behind a TLS-terminating proxy (nginx, ELB, Cloudflare). Tells Django the
# original request was https when the proxy forwards with
# `X-Forwarded-Proto: https`, so request.is_secure() returns True. This is
# what makes Djoser emit `https://...` activation/password-reset links and
# what makes the secure cookies below actually apply.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# With SECURE_PROXY_SSL_HEADER in place, force cookies onto HTTPS only.
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# CORS allowed domains — root domain plus any tenant subdomain.
CORS_ALLOWED_ORIGIN_REGEXES = [
    r'^https?://[a-zA-Z0-9_-]+\.appfinfire\.com$',
    r'^https?://appfinfire\.com$',
]



ALLOWED_FRONTEND_ORIGINS = [
    
]

