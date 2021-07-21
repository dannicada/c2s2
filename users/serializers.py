from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields=['id','email','publickey',]
        read_only_fields = []

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     # first_name = serializers.CharField(required=True)
#     # last_name = serializers.CharField(required=True)
#     email = serializers.EmailField(required=True)
#     class Meta:
#         model=UserModel
#         fields=['id','email','password','first_name','last_name']
#         extra_kwargs = {'password': {'write_only': True}}
