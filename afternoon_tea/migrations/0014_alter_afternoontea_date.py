# Generated by Django 4.0.8 on 2023-02-05 23:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afternoon_tea', '0013_alter_afternoontea_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afternoontea',
            name='date',
            field=models.DateField(choices=[(datetime.date(2023, 3, 4), 'Sat: Mar 04'), (datetime.date(2023, 3, 5), 'Sun: Mar 05'), (datetime.date(2023, 3, 11), 'Sat: Mar 11'), (datetime.date(2023, 3, 12), 'Sun: Mar 12'), (datetime.date(2023, 3, 18), 'Sat: Mar 18'), (datetime.date(2023, 3, 19), 'Sun: Mar 19')]),
        ),
    ]