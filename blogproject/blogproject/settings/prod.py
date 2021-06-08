from .base import *
DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'miniapp.zhuyinze.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_blog',
        'USER': 'root',
        'PASSWORD': 'Yuncan@1602',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
