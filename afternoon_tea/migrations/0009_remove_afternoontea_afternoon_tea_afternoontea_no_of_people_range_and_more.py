# Generated by Django 4.1 on 2022-11-16 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('afternoon_tea', '0008_alter_afternoontea_time'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='afternoontea',
            name='afternoon_tea_afternoontea_no_of_people_range',
        ),
        migrations.AddField(
            model_name='afternoontea',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tea_order', to='profiles.userprofile'),
        ),
        migrations.AddConstraint(
            model_name='afternoontea',
            constraint=models.CheckConstraint(check=models.Q(('no_of_people__range', (1, 6))), name='afternoon_tea_afternoontea_no_of_people_range'),
        ),
    ]