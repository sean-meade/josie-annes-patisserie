# Generated by Django 4.1 on 2022-11-25 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afternoon_tea', '0010_remove_afternoontea_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afternoontea',
            name='date',
            field=models.DateField(choices=[(datetime.date(2022, 12, 17), 'Sat: Dec 17'), (datetime.date(2022, 12, 18), 'Sun: Dec 18'), (datetime.date(2022, 12, 24), 'Sat: Dec 24'), (datetime.date(2022, 12, 25), 'Sun: Dec 25'), (datetime.date(2022, 12, 31), 'Sat: Dec 31'), (datetime.date(2023, 1, 1), 'Sun: Jan 01')]),
        ),
    ]