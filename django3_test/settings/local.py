#!/usr/env/bin python
# -*- coding: utf-8 -*-

# @Time    : 2020/4/26 22:44|22:44
# @Author  : yangdingyi
# @File    : local
# @Software: PyCharm

from .base import *

print('settings.local')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': env.str('DJANGO_SQLITE3_URL', default=str(ROOT_DIR.path('db.sqlite3'))),
    }
}
