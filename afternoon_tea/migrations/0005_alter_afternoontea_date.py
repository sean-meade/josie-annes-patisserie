# Generated by Django 4.1 on 2022-11-16 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afternoon_tea', '0004_alter_afternoontea_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afternoontea',
            name='date',
            field=models.DateField(choices=[(datetime.date(2022, 12, 10), 'Sat: Dec 10'), (datetime.date(2022, 12, 11), 'Sun: Dec 11'), (datetime.date(2022, 12, 17), 'Sat: Dec 17'), (datetime.date(2022, 12, 18), 'Sun: Dec 18'), (datetime.date(2022, 12, 24), 'Sat: Dec 24'), (datetime.date(2022, 12, 25), 'Sun: Dec 25')]),
        ),
    ]
