from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .models import Message,Medicine,Medicament
from .serializers import MessageSerializer,CustomUserSerializer,MedicineSerializer,MedicamentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class MessageViewet(ModelViewSet):

    serializer_class = MessageSerializer
    model= Message


    def get_queryset(self):

        return Message.objects.all()
    
    @action(detail=False, methods=['POST'])
    def conversation(self, request):
        sender = request.data.get('sender')
        receiver = request.data.get('receiver')
        
        
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
    
    

        
class ConversationViewSet(ReadOnlyModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(Q(sender=user) | Q(receiver=user)).distinct()


class UserViewSet(ReadOnlyModelViewSet):
    
    serializer_class = CustomUserSerializer
    parser_classes = [IsAuthenticated]


    def get_queryset(self):
        User = get_user_model()
        return User.objects.filter(username=self.request.user.username).distinct()
    

class MedicineViewset(ModelViewSet):

    serializer_class = MedicineSerializer
    model = Medicine
    
    
    
    def get_queryset(self):

        return Medicine.objects.all()
    
    @action(detail=False, methods=['POST'])
    def prescriptions(self, request):
        sender = request.data.get('sender')
        receiver = request.data.get('receiver')
        
        
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


class MedicamentViewset(ModelViewSet):

    serializer_class = MedicamentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Medicament.objects.all()