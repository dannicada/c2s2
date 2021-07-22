# Generated by Django 3.2.5 on 2021-07-21 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.IntegerField(blank=True, null=True)),
                ('prime', models.IntegerField(blank=True, null=True)),
                ('sender_partial_key', models.IntegerField(blank=True, null=True)),
                ('reciever_partial_key', models.IntegerField(blank=True, null=True)),
                ('sender_private_key', models.IntegerField(blank=True, null=True)),
                ('reciever_private_key', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
