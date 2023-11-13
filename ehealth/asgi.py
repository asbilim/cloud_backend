import os

from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from chat.routing import urlpatterns


asgi_application =  get_asgi_application()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ehealth.settings')

application = ProtocolTypeRouter({
    "http":asgi_application,
    "websocket":
        AuthMiddlewareStack(
            URLRouter(
                urlpatterns
            )
        )
    
})
