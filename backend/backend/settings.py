"""
Settings file that depend on environment variables.

Set these:

1. `SECRET_KEY` (`str`)
2. `DEBUG` (`bool`, defaults to `False`)
"""

import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = os.environ("SECRET_KEY")

DEBUG = True if os.environ["DEBUG"] else False

if not SECRET_KEY and not DEBUG:
    raise RuntimeError("If DEBUG isn't specifically passed in, you need to specify a SECRET_KEY.")

ALLOWED_HOSTS = ["*"]

#
# Application definition.
#

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "data_mine",
    "meme_bank",
    "game_state",
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

# Templates are not used in this project.

TEMPLATES = []

WSGI_APPLICATION = "backend.wsgi.application"

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

# Passwords are only used for admin accounts.

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

#
# Internationalization configuration.
#

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

#
# Static files.
#

STATIC_URL = "/static/"
