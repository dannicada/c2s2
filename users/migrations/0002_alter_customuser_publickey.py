# Generated by Django 3.2.5 on 2021-07-21 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='publickey',
            field=models.BigIntegerField(null=True, unique=True),
        ),
    ]
