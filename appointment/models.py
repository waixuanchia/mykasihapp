from django.db import models
from officers.models import officer
from accounts.models import User


# Create your models here.

class Appointment(models.Model):
    id = models.UUIDField(primary_key=True)
    appointment_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    meeting_link = models.TextField(null=True,blank=True)
    counsellor = models.ForeignKey(officer,on_delete=models.SET_NULL)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    completed = models.BooleanField(null=True,blank=True)
    unattend = models.BooleanField(null=True,blank=True)
    

