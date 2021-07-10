from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
# Create your models here.



class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    publickey = models.BigIntegerField()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Secret(models.Model):
    secrete_key = models.IntegerField(blank=True, null=True)
    # sender = models.ForeignKey(to=CustomUser, null=True, on_delete=models.SET_NULL)
    # reciever = models.ForeignKey(to=CustomUser, null=True, on_delete=models.SET_NULL)