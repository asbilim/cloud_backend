from django.shortcuts import render,HttpResponse
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Doctors
from .serializers import DoctosSerializer
def home(request):
    

    create_15_doctors()
    return render(request,'listings/home.html')


class DoctorsViewSet(ModelViewSet):

    serializer_class = DoctosSerializer

    queryset = Doctors.objects .all()