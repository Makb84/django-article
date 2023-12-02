"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for the 'config' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Create a WSGI application using the Django application
application = get_wsgi_application()
