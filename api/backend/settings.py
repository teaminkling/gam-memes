"""
Settings file that depend on environment variables.

Set these:

1. `SECRET_KEY` (`str`, mandatory if not `DEBUG`, otherwise defaults to a UUID4 string).
2. `DEBUG` (`bool`, defaults to `False`).
"""

import os

from pathlib import Path
from uuid import uuid4


PROJECT_TITLE = "memeware.io"

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = True if os.environ.get("DEBUG") else False

if not SECRET_KEY and not DEBUG:
    raise RuntimeError(
        "If DEBUG isn't specifically passed in, you need to specify a SECRET_KEY."
    )
elif not SECRET_KEY:
    # Generate a secret key if debug because it doesn't matter. Not recommended as you will need
    # to clear your cookies every time you re-run the server.

    SECRET_KEY = str(uuid4())

ALLOWED_HOSTS = [
    "memeware.io",
    "localhost",
    "127.0.0.1",
]

#
# Application definition.
#

INSTALLED_APPS = [
    "grappelli",
    "rest_framework",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "game_state",
    "data_mine",
    "meme_bank",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

# The server needs templates if using the admin application, which we are.

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "backend.wsgi.application"

ASGI_APPLICATION = "backend.asgi.application"

#
# Database configuration.
#

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

#
# Password validation.
#

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

#
# Admin
#

GRAPPELLI_ADMIN_TITLE = f"{PROJECT_TITLE} Project Administration"

#
# DRF
#

# Use Django's standard `django.contrib.auth` permissions, or allow read-only access.

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
    ],
}

#
# Internationalization configuration.
#

LANGUAGE_CODE = "en-au"

TIME_ZONE = "Australia/Melbourne"

USE_I18N = True

USE_L10N = True

USE_TZ = True

#
# Static files.
#

STATIC_URL = "/static/"
STATIC_ROOT = "static"
