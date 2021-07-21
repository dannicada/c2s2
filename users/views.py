from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework import generics, serializers, status,permissions
from dj_rest_auth.views import (LoginView, LogoutView, PasswordChangeView, UserDetailsView)
from django.contrib.auth import get_user_model

UserModel = get_user_model()

# Create your views here.




class UserView(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny, ]
    queryset = UserModel.objects.all()

    def create(self, request, *args, **kwargs):
        """
        create a new Exchange
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)