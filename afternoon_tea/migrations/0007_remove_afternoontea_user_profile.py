# Generated by Django 4.1 on 2022-11-16 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afternoon_tea', '0006_afternoontea_booking_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='afternoontea',
            name='user_profile',
        ),
    ]