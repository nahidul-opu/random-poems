"""
WSGI config for djangoProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

from whitenoise.django import DjangoWhiteNoise
from django.core.wsgi import get_wsgi_application
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xxxx.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
