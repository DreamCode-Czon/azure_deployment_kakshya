# """
# WSGI config for django_project project.
#
# It exposes the WSGI callable as a module-level variable named ``application``.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
# """
#
#
from django.core.wsgi import get_wsgi_application
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
# if os.environ.get('DJANGO_ENV') == 'production':
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'azuresite.production')
# else:
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'azuresite.settings')
application = get_wsgi_application()
