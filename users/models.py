from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.deletion import SET_NULL
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=True)
    publickey = models.BigIntegerField(unique=True, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


    def __str__(self):              # __unicode__ on Python 2
        return self.email

class Secret(models.Model):
    secrete_key = models.IntegerField(blank=True, null=True)
    # sender = models.ForeignKey(to=CustomUser, null=True, on_delete=models.SET_NULL)
    # reciever = models.ForeignKey(to=CustomUser, null=True, on_delete=models.SET_NULL)