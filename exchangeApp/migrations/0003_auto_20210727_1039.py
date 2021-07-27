# Generated by Django 3.2.5 on 2021-07-27 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exchangeApp', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='reciever',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recieved_exchange', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_exchange', to=settings.AUTH_USER_MODEL),
        ),
    ]
