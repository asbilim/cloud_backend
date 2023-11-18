from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
import json
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async
class ChatConsumer(AsyncWebsocketConsumer):

    
    
    async def connect(self):

        self.sender = self.scope['url_route']['kwargs']['sender']
        self.receiver = self.scope['url_route']['kwargs']['receiver']
        
        self.room_group_layer = f"{self.scope['url_route']['kwargs']['sender']}_{self.scope['url_route']['kwargs']['receiver']}"
        
        await self.channel_layer.group_add(
            self.room_group_layer,
            self.channel_name
        )
        

        await self.accept()

    async def disconnect(self, close_code):
        
        await self.channel_layer.group_discard(
            self.room_group_layer,
            self.channel_name
        )
        

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        User = get_user_model()
        sender = await sync_to_async(User.objects.get)(username=self.sender)
        receiver = await sync_to_async(User.objects.get)(username=self.receiver)

        # Save the message in the database
        message = await sync_to_async(Message.objects.create)(
            sender=sender,
            receiver=receiver,
            content=message
        )

        print(message)

        # Send the message to the room group
        await self.channel_layer.group_send(
            self.room_group_layer,
            {
                'type': 'chat_message',
                'message': message,
                'sender': self.sender,
                'receiver':message.receiver.username,
                'date':str(message.date),
                'delivered':message.delivered
            }
        )

    async def chat_message(self, event):
        print("sending message")
        message = event['message']
        sender = event['sender']

        # Send the message to the WebSocket
        await self.send(json.dumps({
            'message': message.content,
            'sender':sender,
            'receiver':message.receiver.username,
            'date':str(message.date),
            'delivered':message.delivered
        }))