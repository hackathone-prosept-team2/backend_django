import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", default=get_random_secret_key())
DEBUG = os.getenv("DEBUG", default="False") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", default="127.0.0.1").split(", ")
CSRF_TRUSTED_ORIGINS = os.getenv("TRUSTED_ORIGINS", default="").split(", ")
# CORS_ALLOWED_ORIGINS = os.getenv("TRUSTED_ORIGINS", default="").split(", ")
CORS_ALLOW_ALL_ORIGINS = True

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    # "rest_framework_simplejwt",
    "djoser",
    "drf_spectacular",
    "corsheaders",
]

LOCAL_APPS = [
    "apps.users.apps.UsersConfig",
    "apps.products.apps.ProductsConfig",
    "apps.dealers.apps.DealersConfig",
    "apps.prices.apps.PricesConfig",
    "apps.api.apps.ApiConfig",
]

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_NAME", default="postgres"),
        "USER": os.getenv("POSTGRES_USER", default="postgres"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", default="postgres"),
        "HOST": os.getenv("POSTGRES_HOST", default="db"),
        "PORT": os.getenv("POSTGRES_PORT", default=5432),
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
]

# Internationalization

LANGUAGE_CODE = "ru"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Users

AUTH_USER_MODEL = "users.CustomUser"
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", default="admin@admin.admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", default="Password-123")

# Other settings

SPECTACULAR_SETTINGS = {
    "TITLE": "API для сервиса сопоставления артикулов Просепт. Команда 2",
    "DESCRIPTION": "Проект разработан в рамках Яндекс-Хакатона: Просепт",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SCHEMA_PATH_PREFIX": "/api/v1/",
    "SWAGGER_UI_DIST": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.3",
}

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend"
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DATE_INPUT_FORMATS": ["%d.%m.%Y"],
    "DATE_FORMAT": "%d.%m.%Y",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

DJOSER = {
    "HIDE_USERS": False,
    "PERMISSIONS": {
        "user_list": [
            "rest_framework.permissions.IsAuthenticated",
        ],
        "user": [
            "rest_framework.permissions.IsAuthenticated",
        ],
    },
    "SERIALIZERS": {
        "user_create": "apps.api.v1.users.serializers.CreateUserSerializer",
        "user": "apps.api.v1.users.serializers.UserListSerializer",
        "current_user": "apps.api.v1.users.serializers.UserListSerializer",
    },
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    # "loggers": {
    #     "django.db.backends": {
    #         "level": "DEBUG",
    #         "handlers": ["console"],
    #     }
    # },
}
