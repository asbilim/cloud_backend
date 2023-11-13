from rest_framework.routers import SimpleRouter
from django.urls import path,include
from .views import DoctorsViewSet

router = SimpleRouter()
router.register('doctors',DoctorsViewSet,basename="doctors")

urlpatterns = [
    path('api/',include(router.urls))
]
