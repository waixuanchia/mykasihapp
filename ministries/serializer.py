from rest_framework.serializers import ModelSerializer
from .models import Ministries,Regions


class RegionSerializer(ModelSerializer):
    class Meta:
        model = Regions
        fields = ['id','types']

class MinistrySerializer(ModelSerializer):
    region = RegionSerializer(required=True)
    class Meta:
        model = Ministries
        fields = ['id','office','address','tels','faks','emel','latitude','longitude','region']


        


