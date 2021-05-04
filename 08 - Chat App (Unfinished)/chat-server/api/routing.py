from django.urls import path
from .consumers import WSConsumer

websocket_urlpatterns = [path("api/v1/front/", WSConsumer.as_asgi())]
