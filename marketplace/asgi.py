import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter


django_asgi_app = get_asgi_application()
os.environ.setdefault('DJANGO_SETTING_MODULE','marketplace.settings')
application = ProtocolTypeRouter({
    'http':django_asgi_app,
})

ASGI_APPLICATION = 'marketplace.asgi.application'