# Generated by Django 3.2.5 on 2021-07-22 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeApp', '0003_auto_20210722_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='sender_private_key',
            field=models.BigIntegerField(default=324433),
            preserve_default=False,
        ),
    ]