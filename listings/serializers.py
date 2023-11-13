from rest_framework.serializers import ModelSerializer
from .models import Doctors

class DoctosSerializer(ModelSerializer):

    class Meta:

        model = Doctors
        fields = ["username","profile","description","ratings","consultation_fee","description","id"]