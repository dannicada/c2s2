# Generated by Django 3.2.5 on 2021-07-22 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeApp', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='base',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='prime',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='reciever_partial_key',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='reciever_private_key',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='sender_partial_key',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='sender_private_key',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]