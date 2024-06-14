"""
ASGI config for conquermanager project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
# Para cuando desplegemos el proyecto. (asíncronos)

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conquermanager.settings')

application = get_asgi_application()
