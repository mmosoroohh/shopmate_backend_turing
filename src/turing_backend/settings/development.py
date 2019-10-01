from .base import *
import os

DEBUG = True
TESTING = False

STRIPE_API_KEY = "sk_test_R8c2wrOPgJbwK8C0nw3E8ULg00TWOB23H2"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),      # replace with root
        'PASSWORD': os.getenv('DB_PASSWORD'),   # replace with root
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
    }
}

SOCIAL_AUTH_FACEBOOK_KEY = '860025437682601'
SOCIAL_AUTH_FACEBOOK_SECRET = 'c9e546a49cfe53c030faf43adb83765c'
