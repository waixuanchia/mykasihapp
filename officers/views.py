from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import officer, Role
from .serializer import officerSerializer,roleSerializer



# Create your views here.

class officerViewSet(viewsets.ModelViewSet):
    queryset = officer.objects.all()
    
    serializer_class = officerSerializer
    permission_classes = [AllowAny]

    def create(self,request):
        print(request.data)
        
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            print(serializer.validated_data)

        message = {"message":"officer created"}
        return Response(message)
    
class roleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = roleSerializer
    permission_classes = [AllowAny]

    
    def list(self,request):
        roles = self.get_queryset()
        serializer = self.get_serializer(instance=roles,many=True)
        data = serializer.data
        return Response(data)



