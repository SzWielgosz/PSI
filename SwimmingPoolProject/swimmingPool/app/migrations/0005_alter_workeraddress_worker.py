# Generated by Django 4.1.3 on 2022-11-13 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_client_adress_clientadress_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workeraddress',
            name='worker',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.worker'),
        ),
    ]