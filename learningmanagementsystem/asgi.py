import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import mentor.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learningmanagementsystem.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            mentor.routing.websocket_urlpatterns
        )
    )
})


