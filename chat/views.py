from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Message
from .serializers import MessageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.db.models import Q
class MessageViewet(ModelViewSet):

    serializer_class = MessageSerializer
    model= Message


    def get_queryset(self):

        return Message.objects.all()
    
    @action(detail=False, methods=['POST'])
    def conversation(self, request):
        sender = request.data.get('sender')
        receiver = request.data.get('receiver')
        print("this are the datas",sender,receiver)
        
        try:
            sender = get_user_model().objects.get(username=sender)
            receiver = get_user_model().objects.get(username=receiver)
        except Exception as e:
            print(e)

        

        queryset = self.get_queryset().filter(
            (Q(sender=sender) & Q(receiver=receiver)) | (Q(sender=receiver) & Q(receiver=sender))
        )
        serializer = self.get_serializer(queryset, many=True)
        
        return Response(serializer.data)
        
    
