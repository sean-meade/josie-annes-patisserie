# Generated by Django 4.1 on 2022-11-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afternoon_tea', '0002_afternoontea_time_alter_afternoontea_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afternoontea',
            name='time',
            field=models.CharField(choices=[('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00')], default='green', max_length=6),
        ),
    ]
