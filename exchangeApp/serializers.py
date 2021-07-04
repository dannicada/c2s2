from rest_framework import serializers
from .models import *

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Exchange
        fields = '__all__'
        read_only_fields = []
