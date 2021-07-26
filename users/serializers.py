from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from dj_rest_auth.serializers import (LoginSerializer, PasswordResetSerializer)


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields=['id','email','publickey','first_name', 'last_name']
        read_only_fields = []

class UserRegistrationSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField(required=True)
    # last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    class Meta:
        model=User
        fields=['id','email','password','publickey',]
        extra_kwargs = {'password': {'write_only': True}}

class UserLoginSerializer(LoginSerializer):
    username = None