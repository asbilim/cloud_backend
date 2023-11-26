

from .consumer import ChatConsumer
from django.urls import path,re_path


urlpatterns = [
    path('ws/chats/<str:sender>/<str:receiver>/',ChatConsumer.as_asgi()),
    path('ws/chats/<str:sender>/<str:receiver>/<int:inverse>/',ChatConsumer.as_asgi()),

]
