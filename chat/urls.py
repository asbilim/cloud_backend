from django.urls import path,include
from rest_framework.routers import SimpleRouter
from chat.views import MessageViewet

router = SimpleRouter()

router.register('conversations',MessageViewet,basename="conversations")
urlpatterns = [
    path('chats/',include(router.urls))
]
