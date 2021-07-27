from django.db import models
from users.models import *
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator


User = get_user_model()

# Create your models here.


class Exchange(models.Model):
    base = models.PositiveIntegerField(blank=True, null=True)
    prime = models.PositiveIntegerField(blank=True, null=True)
    sender = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='sent_exchange')
    reciever = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='recieved_exchange')
    sender_partial_key = models.PositiveIntegerField(blank=True, null=True)
    reciever_partial_key = models.PositiveIntegerField(blank=True, null=True)
    sender_private_integer = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    reciever_private_integer = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(9999)])
    message = models.CharField(null=False, blank=False, max_length=300)
    encrypted_message = models.CharField(null=True, blank=True, max_length=3000)
