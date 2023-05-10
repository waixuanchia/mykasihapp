from django.db import models
from accounts.models import User

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=250,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class officer(models.Model):
    user = models.OneToOneField(User,related_name="officer",on_delete=models.CASCADE)
    role = models.OneToOneField(Role,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)



