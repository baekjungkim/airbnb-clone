import os  # noqa
from .base import *  # noqa

SECRET_KEY = os.environ.get("DJANGO_PRD_SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DJANGO_DB_ENGINE"),
        "NAME": os.environ.get("DJANGO_DB_PRD_NAME"),
        "USER": os.environ.get("DJANGO_DB_PRD_USERNAME"),
        "PASSWORD": os.environ.get("DJANGO_DB_PRD_PASSWORD"),
        "HOST": os.environ.get("DJANGO_DB_PRD_HOST"),
        "PORT": os.environ.get("DJANGO_DB_PRD_PORT"),
    }
}
