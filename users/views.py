from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.generics import RetrieveAPIView
from rest_framework import generics, serializers, status, permissions
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from dj_rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView, UserDetailsView)
from django.db import IntegrityError

UserModel = get_user_model()

# Create your views here.


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny, ]
    queryset = UserModel.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'

    def create(self, request, *args, **kwargs):
        """
        create a new User
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())

        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        if len(self.kwargs) is 0:
            self.kwargs[lookup_url_kwarg] = str(self.request.user.id)
            print(self.kwargs)


        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        # Perform the lookup filtering.
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except IntegrityError:
            return Response({'detail': 'User with that email already exists.'}, status=status.HTTP_409_CONFLICT)
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
