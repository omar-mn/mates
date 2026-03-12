from .consumer import MessageConsumer
from django.urls import path

ws_urls= [
    path('ws/message/' , MessageConsumer.as_asgi()),
]