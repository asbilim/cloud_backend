from rest_framework.routers import SimpleRouter
from django.urls import path,include
from .views import DoctorsViewSet

router = SimpleRouter()
router.register('doctors',DoctorsViewSet,basename="doctors")

urlpatterns = [
    path('api/',include(router.urls)),
    path('api/',include('chat.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    
]
