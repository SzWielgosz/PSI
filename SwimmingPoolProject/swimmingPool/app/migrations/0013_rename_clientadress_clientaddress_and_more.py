# Generated by Django 4.1.3 on 2022-11-29 14:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_ticket_dateofpurchase'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientAdress',
            new_name='ClientAddress',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='dateOfPurchase',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 29, 15, 38, 32, 580452)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='worker',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='app.worker'),
        ),
    ]
