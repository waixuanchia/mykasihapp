from rest_framework.serializers import ModelSerializer
from .models import Report, Status
from accounts.serializer import UserSerializer
from ministries.serializer import MinistrySerializer

class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = ['id','status']


class ReportSerializer(ModelSerializer):
    user = UserSerializer(required=False)
    ministry = MinistrySerializer(required=False)
    status = StatusSerializer(required=False)
    class Meta:
        model = Report
        fields = ['id','user','image_url','ministry','status','description','created_at']
