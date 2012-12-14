# Based on: https://github.com/zsiciarz/django-envelope/blob/master/runtests.py

import os

from django.conf import settings
from django.core.management import call_command

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS=(
            'javascript_settings',
        ),
    )

call_command('test', 'javascript_settings')
