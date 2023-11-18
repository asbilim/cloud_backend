from rest_framework.serializers import ModelSerializer
from .models import Message
from django.contrib.auth import get_user_model

class UserSerializer(ModelSerializer):

    class Meta:

        model = get_user_model()
        fields = ['id','username']
class MessageSerializer(ModelSerializer):

    receiver = UserSerializer()
    sender = UserSerializer()

    class Meta:
        
        model = Message
        fields = ['sender','receiver','content','date','delivered','id']
        

        