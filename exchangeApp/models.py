from django.db import models
from users.models import *
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Exchange(models.Model):
    base = models.IntegerField(blank=True, null=True)
    prime = models.IntegerField(blank=True, null=True)
    sender = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='exchange_sender')
    reciever = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='exchange_reciever')
    sender_partial_key = models.IntegerField(blank=True, null=True)
    reciever_partial_key = models.IntegerField(blank=True, null=True)
    sender_private_key = models.IntegerField(blank=True, null=True)
    reciever_private_key = models.IntegerField(blank=True, null=True)
