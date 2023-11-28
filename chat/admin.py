from django.contrib import admin
from .models import Message,Medicine,Medicament

admin.site.register(Message)
admin.site.register(Medicament)
admin.site.register(Medicine)