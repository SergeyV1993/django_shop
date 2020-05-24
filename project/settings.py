import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '-r)97n$0o@kx%vlav1u@vqfo8aut^*jx1%jrktbw2x4l2whs=9'
DEBUG = True
ALLOWED_HOSTS = []

'''
# Для вывода на прод (передавать в докере)

SECRET_KEY = os.environ.get("SECRET_KEY_SHOP")
DEBUG = int(os.environ.get("DEBUG", default=0))
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
'''

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # my_apps
    'backend.registration',
    'backend.orders',
    'backend.products',
    'backend.home',
    'backend.shop',
    'backend.cart',
    'backend.categories',
    'backend.account.apps.AccountConfig',
    'backend.login',
    'backend.discount',
    'backend.search',

    'debug_toolbar',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'backend.categories.middleware.GetCategory',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'backend.cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'OPTIONS': {
            'timeout': 20,
        }
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 25
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s: %(message)s \n',
            'datefmt': '%Y.%m.%d %H:%M:%S',
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(BASE_DIR + '/logs', 'test.log'),
        },
        # для вывода логов в консоль
        # 'console': {
        #    'class': 'logging.StreamHandler',
        #    'formatter': 'simple',
        # },
        'file_sql': {
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(BASE_DIR + '/logs', 'file_sql.log'),
        },

    },
    'loggers': {
        'django': {
            'level': 'CRITICAL',
            'handlers': ['file'],
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['file_sql'],
        },
        'django.request': {
            'level': 'ERROR',
            'handlers': ['file'],
        }
    }
}

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'
'''
# запускать аккуратно, только после запуска redis-server или докера, иначе будет ошибка
REDIS_HOST = '0.0.0.0'
REDIS_PORT = '6379'

CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'


CACHES = {
    'default': {
    
        # "BACKEND": 'django.core.cache.backends.locmem.LocMemCache', #сохраняет кэш в оперативке
        # "BACKEND": 'django.core.cache.backends.dummy.DummyCache', #не сохраняет кэш, нужен для отладки
        
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/1',
        "TIMEOUT": 60 * 60, # живучесть кэша в секундах
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "MAX_ENTRIES": 400, # количество обращений к кэшу, пока он не обновится
        }
    }
}
'''
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

if DEBUG:
    INTERNAL_IPS = ('127.0.0.1', 'localhost',)
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
