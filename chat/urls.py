from django.urls import path,include
from rest_framework.routers import SimpleRouter
from chat.views import MessageViewet,ConversationViewSet,UserViewSet,MedicineViewset,MedicamentViewset
router = SimpleRouter()

router.register('conversations',MessageViewet,basename="conversations")
router.register('inbox',ConversationViewSet,basename="inbox")
router.register('me',UserViewSet,basename="user-info")
router.register('medicine',MedicineViewset,basename="prescriptions")
router.register('medicaments',MedicamentViewset,basename="medicaments")

urlpatterns = [
    path('chats/',include(router.urls))
]
