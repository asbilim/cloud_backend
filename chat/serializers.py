from rest_framework.serializers import ModelSerializer
from .models import Message,Medicament,Medicine
from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers

class CustomUserSerializer(BaseUserSerializer):
    profile = serializers.ImageField(read_only=True)

    class Meta(BaseUserSerializer.Meta):
        fields = tuple(BaseUserSerializer.Meta.fields) + ('profile',)


class UserSerializer(ModelSerializer):

    class Meta:

        model = get_user_model()
        fields = ['id','username','profile']
class MessageSerializer(ModelSerializer):

    receiver = UserSerializer()
    sender = UserSerializer()

    class Meta:
        
        model = Message
        fields = ['sender','receiver','content','date','delivered','id']
    

class MedicamentSerializer(ModelSerializer):

    class Meta:

        model = Medicament
        fields = ["id","name","form","strenght"]


        

class MedicineSerializer(ModelSerializer):

    medicaments = MedicamentSerializer(many=True)
    receiver = UserSerializer()
    sender = UserSerializer()
    class Meta:

        model = Medicine
        fields = "__all__"