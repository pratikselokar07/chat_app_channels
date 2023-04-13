"""
ASGI config for chat_app_channel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from . import routing
import channels
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app_channel.settings')


application = channels.routing.ProtocolTypeRouter({
    'http' : get_asgi_application(),
    "websocket": URLRouter(
            routing.websocket_urlpatterns
        )
})