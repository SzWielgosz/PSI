# Generated by Django 4.1.3 on 2022-11-29 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_shift_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='description',
            field=models.CharField(choices=[('FIRST_SHIFT', '1 zmiana'), ('SECOND_SHIFT', '2 zmiana')], max_length=12),
        ),
    ]