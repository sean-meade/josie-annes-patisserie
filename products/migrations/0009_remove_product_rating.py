# Generated by Django 4.1 on 2022-12-21 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_sku'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]
