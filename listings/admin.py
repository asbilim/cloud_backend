from django.contrib import admin
from .models import People,Doctors
from django.contrib.auth import get_user_model


User = get_user_model()
admin.site.register(Doctors)
admin.site.register(User)

