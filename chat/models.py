from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()
class Message(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    delivered = models.BooleanField(default=False)
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender")
    receiver = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.sender} sent to {self.receiver} {self.content[0:10]}..."

    
    class Meta:

        ordering = ('date','date')


class Medicament(models.Model):

    medicine_forms = (("tablet","tablet"),("injections","injections"),("suspension","suspension"),("capsule","capsule"))

    name = models.CharField(max_length=255)
    form = models.CharField(max_length=255,choices=medicine_forms)
    strenght = models.IntegerField()

    def __str__(self):

        return self.name



class Medicine(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    medicaments = models.ManyToManyField(Medicament)
    delivered = models.BooleanField(default=False)
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name="prescriptions")
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name="prescript")

    def __str__(self):

        return f"{self.sender} sent to {self.receiver}"

    
    class Meta:

        ordering = ('date','date')