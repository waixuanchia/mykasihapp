from django.db import models

# Create your models here.
class Regions(models.Model):
    types = models.CharField(max_length=120,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.types

class Ministries(models.Model):
    office = models.CharField(max_length=120,blank=False,null=False)
    address = models.TextField(blank=True,null=True)
    tels = models.CharField(max_length=120,blank=True,null=True)
    faks = models.CharField(max_length=120,blank=True,null=True)
    emel = models.CharField(max_length=120,blank=True,null=True)
    latitude = models.CharField(max_length=120,blank=True,null=True)
    longitude = models.CharField(max_length=120,blank=True,null=True)
    region = models.ForeignKey(Regions,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.office

 


    
