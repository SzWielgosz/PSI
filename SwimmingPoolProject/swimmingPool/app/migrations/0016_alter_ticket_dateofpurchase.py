# Generated by Django 4.1.3 on 2022-11-29 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_ticket_client_alter_ticket_dateofpurchase_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='dateOfPurchase',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 29, 15, 56, 11, 294568)),
        ),
    ]
