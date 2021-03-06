"""Staging settings and globals."""

from __future__ import absolute_import

from os import environ

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME','courtfinder_search'),
        'USER': os.getenv('DB_USER', 'courtfinder'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', '5432'),
    },
    '_tmp': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '_tmp',
        'USER': os.getenv('DB_USER', 'courtfinder'),
        'PASSWORD': os.getenv('DB_PASSWORD','C1cwG3P7n2'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

ALLOWED_HOSTS = '*'

COURTFINDER_ADMIN_HEALTHCHECK_URL = 'https://courtfinder.is.dsd.io/admin/healthcheck.json'
COURTS_DATA_S3_URL = 'https://s3-eu-west-1.amazonaws.com/courtfinder-json-staging/courts.json'
