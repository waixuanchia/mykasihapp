from rest_framework import serializers
from .models import officer,Role
from accounts.serializer import UserSerializer

class roleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ("id","role_name")

class officerSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    role = roleSerializer(required=True)

    class Meta:
        model = officer
        fields = "__all__"


