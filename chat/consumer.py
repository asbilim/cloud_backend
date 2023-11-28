from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message,Medicine,Medicament
import json
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async
class ChatConsumer(AsyncWebsocketConsumer):

    
    
    async def connect(self):

        self.sender = self.scope['url_route']['kwargs']['sender']
        self.receiver = self.scope['url_route']['kwargs']['receiver']
        self.inverse = self.scope['url_route']['kwargs']['inverse']
        self.room_group_layer = f"{self.scope['url_route']['kwargs']['sender']}_{self.scope['url_route']['kwargs']['receiver']}"
        
        await self.channel_layer.group_add(
            self.room_group_layer,
            self.channel_name
        )
        
        if self.inverse:

            self.sender,self.receiver = self.receiver,self.sender

        await self.accept()

    async def disconnect(self, close_code):
        
        await self.channel_layer.group_discard(
            self.room_group_layer,
            self.channel_name
        )
        

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        message_type = text_data_json.get('type')
        User = get_user_model()
        sender = await sync_to_async(User.objects.get)(username=self.sender)
        receiver = await sync_to_async(User.objects.get)(username=self.receiver)

        if message_type == 'prescription':
            await self.handle_medicine_message(text_data_json)
        else:
            message = await sync_to_async(Message.objects.create)(
                sender=sender,
                receiver=receiver,
                content=message
            )



            
            await self.channel_layer.group_send(
                self.room_group_layer,
                {
                    'type': 'chat_message',
                    'message': message,
                    'sender': json.dumps([{"username":sender.username,"profile":sender.profile.url}]),
                    'receiver':json.dumps([{"username":receiver.username,"profile":receiver.profile.url}]),
                    'date':str(message.date),
                    'delivered':message.delivered
                }
            )


    async def chat_message(self, event):
       
        message = event['message']
        sender = event['sender']


        await self.send(json.dumps({
            'message': message.content,
            'sender':sender,
            'receiver':message.receiver.username,
            'date':str(message.date),
            'delivered':message.delivered
        }))
        
    async def medicine_message(self, event):
       
        await self.send(json.dumps({
            'type': 'medicine_message',
            'data': event['medicine_info']
        }))


    async def handle_medicine_message(self, data):
        
        medicament_ids = data['medicament_ids']
        sender_username = self.sender
        receiver_username = self.receiver

        
        User = get_user_model()
        sender = await sync_to_async(User.objects.get)(username=sender_username)
        receiver = await sync_to_async(User.objects.get)(username=receiver_username)

      
        medicine = await sync_to_async(Medicine.objects.create)(
            sender=sender,
            receiver=receiver,
            delivered=False
        )
        
        
        await self.add_medicaments_to_medicine(medicine, medicament_ids)

        medicaments = await sync_to_async(list)(medicine.medicaments.all())
        
        await self.channel_layer.group_send(
            self.room_group_layer,
            {
                'type': 'medicine_message',
                'medicine_info': {
                    'id': medicine.id,
                    'medicaments': [{
                        'id': medicament.id,
                        'name': medicament.name,
                        'form': medicament.form,
                        'strenght': medicament.strenght
                    } for medicament in medicaments],
                    'sender': json.dumps([{"username":sender.username,"profile":sender.profile.url}]),
                    'receiver': json.dumps([{"username":receiver.username,"profile":receiver.profile.url}]),
                    'date': str(medicine.date),
                    'delivered': medicine.delivered
                }
            }
        )
        
    @sync_to_async
    def add_medicaments_to_medicine(self, medicine, medicament_ids):
        for medicament_id in medicament_ids:
            medicament = Medicament.objects.get(id=medicament_id)
            medicine.medicaments.add(medicament)
