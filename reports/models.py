from django.db import models
from accounts.models import User
from ministries.models import Ministries

# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=120,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status


class Report(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    image_url = models.TextField(blank=True,null=True)
    ministry = models.ForeignKey(Ministries,on_delete=models.CASCADE)
    description = models.TextField(blank=True,null=True)


