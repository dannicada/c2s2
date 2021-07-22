from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from .models import Exchange
from rest_framework import generics, serializers, status,permissions

# Create your views here.


class ExchangeView(ModelViewSet):
    serializer_class = ExchangeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    queryset = Exchange.objects.all()


    def create(self, request, *args, **kwargs):
        """
        create a new Exchange
        """
        data = request.data.copy()
        data['sender'] = str(request.user.id)
        print(data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)