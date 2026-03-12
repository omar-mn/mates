import os
from django.core.asgi import get_asgi_application

settings_module = 'Mates.deploy_settings' if 'RENDER_EXTERNAL_HOSTNAME' in os.environ else 'Mates.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter , URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from Messages.routing import ws_urls
from .ws_middleware import jwtAuth


application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        jwtAuth(
            URLRouter(ws_urls)
        )
    ),
})