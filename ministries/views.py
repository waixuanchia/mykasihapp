from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Ministries
from .serializer import MinistrySerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from geopy.distance import geodesic
from functools import reduce
# Create your views here.

class MinistryViewSet(ModelViewSet):
    queryset = Ministries.objects.all()
    serializer_class = MinistrySerializer
    permission_classes = [AllowAny]

    def list(self,request):
        try:
            region = request.query_params['region']
            print(region)
            ministries = Ministries.objects.filter(region__types=region)
            serializer = self.get_serializer(instance=ministries,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            ministries = Ministries.objects.all()
            serializer = self.get_serializer(instance=ministries,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
    @action(methods=['POST'],detail=False)
    def get_nearest_location(self,request):
        location = (request.data['latitude'],request.data['longitude'])
        ministries = Ministries.objects.all()
        serializer = self.get_serializer(instance=ministries,many=True)
        def get_closer_ministry(current_ministry,next_ministry):
            current_ministry_position = (current_ministry['latitude'],current_ministry['longitude'])
            next_ministry_position = (next_ministry['latitude'],next_ministry['longitude'])
            current_ministry_distance = geodesic(current_ministry_position,location)
            next_ministry_distance = geodesic(next_ministry_position,location)

            if current_ministry_distance > next_ministry_distance:
                return next_ministry
            else:
                return current_ministry


        nearest_ministry = reduce(get_closer_ministry,serializer.data)
        return Response(nearest_ministry)
    
    
        
    
        
    
        
    

