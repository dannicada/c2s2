# Generated by Django 3.2.5 on 2021-07-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeApp', '0003_auto_20210727_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchange',
            name='encrypted_message',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]
