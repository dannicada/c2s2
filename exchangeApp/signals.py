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
            instance.base = User.objects.get(id = instance.sender.id).publickey

            # use reciever's publickey as prime/modulo
            instance.prime = User.objects.get(id = instance.reciever.id).publickey

            instance.save()
           
        except Exception as e:
           raise e
    
    else:
        if (instance.reciever_private_integer is not None) and instance.encrypted_message is None:

            # generate sender's partial key
            init_DH_endpoints(instance, instance.base, instance.prime, instance.sender_private_integer, instance.reciever_private_integer, instance.message)
            instance.save()
        else:
            pass