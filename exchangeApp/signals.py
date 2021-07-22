from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from .models import *
from .utils import *
import random


User = get_user_model()


@receiver(post_save, sender=Exchange, dispatch_uid="my_id")
def post_exchange_creation_routine(sender, **kwargs):
    print('\n\nsignal fired\n\n')
    instance, created = kwargs["instance"], kwargs["created"]
    if created:
        try:        
            # use sender's publickey as base
            instance.base = User.objects.get(id = instance.sender).publickey

            # use reciever's publickey as prime/modulo
            instance.prime = User.objects.get(id = instance.reciever).publickey

            instance.save()
           
        except Exception as e:
           raise e
    
    else:
        if instance.reciever_private_key is not None:

            # generate sender's partial key
            init_DH_endpoints(instance, instance.base, instance.prime, instance.sender_private_key, instance.reciever_private_key)
        else:
            pass