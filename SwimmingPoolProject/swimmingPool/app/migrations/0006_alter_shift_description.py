# Generated by Django 4.1.3 on 2022-11-29 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_workeraddress_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='description',
            field=models.CharField(choices=[('FIRST', '1 zmiana'), ('SECOND', '2 zmiana')], max_length=10),
        ),
    ]
