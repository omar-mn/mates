from rest_framework import serializers 
from .models import account
from django.contrib.auth.hashers import make_password


class Sign_UpSerializer(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = ('username' , 'email' , 'password' , 'first_name' , 'last_name' , 'profileImage')

    def create(self, validated_data):
        return account.objects.create(**validated_data)
    
    def validate_password(self, value: str) -> str:
        return make_password(value)
    


class UserInfo(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = ('username' , 'email', 'first_name' , 'last_name' , 'profileImage')