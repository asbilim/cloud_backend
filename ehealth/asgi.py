# isort: skip_file
import os
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ehealth.settings')

asgi_application =  get_asgi_application()
from chat.routing import urlpatterns

application = ProtocolTypeRouter({
    "http":asgi_application,
    "websocket":
        AuthMiddlewareStack(
            URLRouter(
                urlpatterns
            )
        )
    
})
