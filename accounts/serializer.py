from rest_framework.serializers import ModelSerializer
from drf_extra_fields.fields import Base64ImageField
from .models import User,UserProfile

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','username','email','password')

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_active = True
        user.save()
        return user


class UserProfileSerializer(ModelSerializer):
    profile_picture = Base64ImageField()
    user = UserSerializer(required=True)
    class Meta:
        model = UserProfile
        fields = ('id','user','profile_picture','address_line_1','address_line_2','state','city')
