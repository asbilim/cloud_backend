from django.db import models
from django.contrib.auth.models import AbstractUser

class People(AbstractUser):

    consultation_count = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    profile = models.ImageField(upload_to="ehealth/images/doctors/",null=True,blank=True)
    pass


    def __str__(self):

        return self.username


class Doctors(People):

    consultation_fee = models.IntegerField()
    ratings = models.IntegerField(default=0)
    pass

class Patients(People):
    
    personal_notes = models.TextField()

    pass


class Appointment(models.Model):

    patient = models.ForeignKey(Patients,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField()
    is_active = models.BooleanField(default=True)


class Medicine(models.Model):

    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10,decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)


class Prescription(models.Model):

    created_for = models.ForeignKey(Patients,on_delete=models.CASCADE)
    created_by = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    note = models.TextField()
    medicines = models.ManyToManyField(Medicine)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.created_by + " for " + self.created_for