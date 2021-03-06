from .base import *

AWS_SECRETS_MANAGER_SECRET_SECTION = 'inaina:local'
DEBUG = True

ALLOWED_HOSTS += SECRETS['ALLOWED_HOSTS']
DATABASES = SECRETS['DATABASES']

WSGI_APPLICATION = 'config.wsgi.local.application'
