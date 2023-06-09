from .base import *

ALLOWED_HOSTS = ["*"]

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_URL = "/static/"

INTERNAL_IPS = ["127.0.0.1"]
