# Generated by Django 4.2.2 on 2023-07-27 21:42

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribedusers',
            name='subscription_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='subscribedusers',
            name='subscription_expirydate',
            field=models.DateField(default=datetime.date(2023, 8, 26)),
        ),
    ]