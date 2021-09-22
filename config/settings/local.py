# ここにlocal環境だけで動かす時のものを入れていく。

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1', '*']

# ここにlocal環境だけのものを入れていく。
# 下記の例は、mysqlのもの。ENGINEの部分がposgreだと変更が必要。
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django-db',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': 'db',
        'PORT': '3306'
    }
}