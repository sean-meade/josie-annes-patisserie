# Generated by Django 4.1 on 2022-12-16 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_remove_order_delivery_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='collection_date',
            field=models.DateField(blank=True, choices=[(datetime.date(2022, 12, 17), 'Sat: Dec 17'), (datetime.date(2022, 12, 18), 'Sun: Dec 18'), (datetime.date(2022, 12, 19), 'Mon: Dec 19'), (datetime.date(2022, 12, 20), 'Tue: Dec 20'), (datetime.date(2022, 12, 21), 'Wed: Dec 21'), (datetime.date(2022, 12, 22), 'Thu: Dec 22'), (datetime.date(2022, 12, 23), 'Fri: Dec 23'), (datetime.date(2022, 12, 24), 'Sat: Dec 24')], null=True),
        ),
    ]