# Generated by Django 4.1.3 on 2022-11-29 13:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_ticket_dateofpurchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketassignment',
            name='client',
        ),
        migrations.RemoveField(
            model_name='ticketassignment',
            name='ticket',
        ),
        migrations.AddField(
            model_name='shift',
            name='worker',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.worker'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='app.client'),
        ),
        migrations.AlterField(
            model_name='clientadress',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.client'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='dateOfPurchase',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 29, 14, 6, 40, 866950)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='worker',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.worker'),
        ),
        migrations.AlterField(
            model_name='workeraddress',
            name='worker',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.worker'),
        ),
        migrations.DeleteModel(
            name='ShiftAssignment',
        ),
        migrations.DeleteModel(
            name='TicketAssignment',
        ),
    ]
