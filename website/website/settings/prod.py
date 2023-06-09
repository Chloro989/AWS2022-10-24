from .base import *

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default": env.db(),
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files
STATIC_ROOT = "/usr/share/nginx/html/static"
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    "/home/ubuntu/django/lib/python3.10/site-packages/django/contrib/admin/static",
    "/home/ubuntu/MySite/website/static/",
]
