# Generated by Django 4.1 on 2024-01-31 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_alter_order_plated_end_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='plated_end_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 31, 7, 59, 14, 407405)),
        ),
    ]
