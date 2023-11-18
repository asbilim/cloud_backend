from django.db import models
from django.contrib.auth import get_user_model


class Message(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    delivered = models.BooleanField(default=False)
    sender = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="sender")
    receiver = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.sender} sent to {self.receiver} {self.content[0:10]}..."

    
