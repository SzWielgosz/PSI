# Generated by Django 4.1.3 on 2023-01-10 13:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_client_slugfield_alter_ticket_dateofpurchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='dateOfPurchase',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 10, 14, 26, 8, 721356)),
        ),
    ]