

from .consumer import ChatConsumer
from django.urls import path,re_path


urlpatterns = [
    re_path(r'ws/chats/$',ChatConsumer.as_asgi()),
]
