# Generated by Django 3.2.16 on 2023-02-04 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_coupon_object_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='object_price',
        ),
    ]
