# Generated by Django 4.0.8 on 2023-02-04 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]