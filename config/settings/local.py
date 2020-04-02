from config.util import get_server_info_value  # noqa
from .base import *  # noqa

SETTING_PRD_DIC = get_server_info_value("local")
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SETTING_PRD_DIC["SECRET_KEY"]

DEBUG = True

DATABASES = {"default": SETTING_PRD_DIC["DATABASES"]["default"]}
