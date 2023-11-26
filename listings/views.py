from django.shortcuts import render,HttpResponse
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Doctors
from .serializers import DoctorSerializer
def home(request):
    

  
    return render(request,'listings/home.html')


class DoctorsViewSet(ModelViewSet):

    serializer_class = DoctorSerializer

    queryset = Doctors.objects.all()