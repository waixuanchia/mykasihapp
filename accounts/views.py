from django.shortcuts import render
from .models import User,UserProfile
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes,action
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializer import UserSerializer,UserProfileSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]

    #def list(self,request):
        
        
        #response = {"message":"User are not allowed to send this request"}

        #return Response(response,status=status.HTTP_405_METHOD_NOT_ALLOWED)

    #def retrieve(self,request,pk=None):
        #response = {"message":"User are not allowed to send this request"}

        #return Response(response,status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def create(self,request):
        #print(request.data)
        
        #print(self)
        print(request.data)
        user = User.objects.create_user(first_name=request.data['first_name'],
                                   last_name=request.data['last_name'],
                                   username=request.data['username'],
                                   email=request.data['email'],
                                   password=request.data['password'])
        
        user.is_active = True
        user.save()
        
        response = {"message":"User are created"}

        return Response(response,status=status.HTTP_201_CREATED)
    
    #def update(self,request,pk=None):
        #response = {"message":"User are not allowed to send this request"}

        #return Response(response,status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    #def partial_update(self,request,pk=None):
       
        #response = {"message":"User are not allowed to send this request"}

        #return Response(response,status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def delete(self,request,pk=None):
        response = {"message":"User are not allowed to send this request"}
        

        return Response(response,status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]


    

        
    
    


    
