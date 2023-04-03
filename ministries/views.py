from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Ministries
from .serializer import MinistrySerializer
from rest_framework.permissions import AllowAny

# Create your views here.

class MinistryViewSet(ModelViewSet):
    queryset = Ministries.objects.all()
    serializer_class = MinistrySerializer
    permission_classes = [AllowAny]
    

