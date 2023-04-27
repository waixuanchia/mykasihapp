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
        print(request.data)
        userSerializer = self.get_serializer(data=request.data)
        if userSerializer.is_valid():
            try:
                user = userSerializer.create(userSerializer.validated_data)
                response = {"message":"User are created", "user":self.get_serializer(instance=user).data }
                return Response(response,status=status.HTTP_201_CREATED)
            except:
                return Response(response,status=status.HTTP_400_BAD_REQUEST)
        else:
            response = {"message":"The provided data is invalid"}
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
    
    

    
    
    
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


    

        
    
    


    
