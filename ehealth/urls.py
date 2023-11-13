
from django.contrib import admin
from django.urls import path,include
from listings.views import home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ehealth/',include('listings.urls',))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
