import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'info_tbot'),
        'USER': os.getenv('POSTGRES_USER', 'info_tbot'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'info_tbot'),
        'HOST': os.getenv('POSTGRES_HOST', '127.0.0.1'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    },
}
