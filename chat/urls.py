from django.urls import path,include
from rest_framework.routers import SimpleRouter
from chat.views import MessageViewet,ConversationViewSet
router = SimpleRouter()

router.register('conversations',MessageViewet,basename="conversations")
router.register('inbox',ConversationViewSet,basename="inbox")

urlpatterns = [
    path('chats/',include(router.urls))
]
