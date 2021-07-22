from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.generics import RetrieveAPIView
from rest_framework import generics, serializers, status,permissions
from django.contrib.auth import get_user_model
from dj_rest_auth.views import (LoginView, LogoutView, PasswordChangeView, UserDetailsView)
from django.db import IntegrityError

UserModel = get_user_model()

# Create your views here.




class UserView(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny, ]
    queryset = UserModel.objects.all()

    def create(self, request, *args, **kwargs):
        """
        create a new User
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserRegistrationView(generics.CreateAPIView): 
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except IntegrityError:
            return Response({'detail': 'User with that email already exists.'},status=status.HTTP_409_CONFLICT)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RetrieveUserView(RetrieveAPIView):
    queryset = UserModel.objects.all()
    lookup_field = 'email'
    serializer_class = UserSerializer


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UserLoginView(LoginView):
    """
    Check the credentials and return the REST Token
    if the credentials are valid and authenticated.
    Calls Django Auth login method to register User ID
    in Django session framework

    Accept the following POST parameters: username, password
    Return the REST Framework Token Object's key.
    """
    serializer_class = UserLoginSerializer
    queryset = User.objects.all()