from django.db import models
from users.models import *

# Create your models here.


class Exchange(models.Model):
    modulos = models.IntegerField(blank=True, null=True)
    prime = models.IntegerField(blank=True, null=True)
    sender = models.ForeignKey(to=CustomUser, null=True, on_delete=models.SET_NULL, related_name='exchange_sender')
    reciever = models.ForeignKey(to=CustomUser, null=True, on_delete=models.SET_NULL, related_name='exchange_reciever')