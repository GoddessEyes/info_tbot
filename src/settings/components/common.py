import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(
    __file__
)))))

SRC_DIR = os.path.join(BASE_DIR, '..')

_ENV_VAR = 'VAR_PATH'

VAR_PATH = os.getenv(_ENV_VAR, os.path.join(SRC_DIR, 'var'))


SECRET_KEY = 'onv&90%4i0g#64w_*e-q!dmit-dxfe=@fr###ou!0rju85rw+f'

ALLOWED_HOSTS = ('*', )

AUTH_USER_MODEL = 'management.CustomUser'

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'emoji_picker',
    'solo',
)

LOCAL_APPS = (
    'bot',
    'apps.management',
    'apps.static_handlers',
    'apps.buttons',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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
