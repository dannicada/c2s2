from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from .models import *
import random


User = get_user_model()


@receiver(post_save, sender=Exchange, dispatch_uid="my_id")
def post_exchange_creation_routine(sender, **kwargs):
    print('\n\nsignal fired\n\n')
    instance, created = kwargs["instance"], kwargs["created"]
    if created:
        try:        
            # generate 64 bit random number
            user_public_key = random.getrandbits(64)

            # assign random number to user
            instance.publickey = user_public_key
            instance.save()
        except IntegrityError:
            # handle integrity error by generating and assigning new random nuber
            user_public_key = random.getrandbits(64)
            instance.publickey = user_public_key
            pass
    