from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from .models import Exchange
from rest_framework import generics, serializers, status,permissions

# Create your views here.


class CreateExchange(generics.CreateAPIView):
    serializer_class = ExchangeSerializer
    permission_classes = [permissions.AllowAny, ]

    def create(self, request, *args, **kwargs):
        """
        create a new Exchange
        """
        data = request.data.copy()
        data['sender'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)