import os  # noqa: F401
from .base import *  # noqa: F401, F403

SECRET_KEY = os.environ.get("DJANGO_DEV_SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DJANGO_DB_ENGINE"),
        "NAME": os.environ.get("DJANGO_DB_DEV_NAME"),
        "USER": os.environ.get("DJANGO_DB_DEV_USERNAME"),
        "PASSWORD": os.environ.get("DJANGO_DB_DEV_PASSWORD"),
        "HOST": os.environ.get("DJANGO_DB_DEV_HOST"),
        "PORT": os.environ.get("DJANGO_DB_DEV_PORT"),
    }
}
