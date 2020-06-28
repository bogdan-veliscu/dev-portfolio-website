from .base import *

DEBUG = False
ALLOWED_HOSTS = [
    '.mumchef.io', 'mumchef.io', '.codeswiftr.com', 'codeswiftr.com'
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mumchef_io',
        'USER': 'mumchef_user',
        'PASSWORD': '$P@S*AhFGte%6wRhtJhgef^jBnCQs9',
        'HOST': 'localhost',
        'PORT': '',
    }
}
