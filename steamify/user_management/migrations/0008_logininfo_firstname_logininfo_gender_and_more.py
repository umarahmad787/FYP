# Generated by Django 4.2.2 on 2023-07-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0007_alter_logininfo_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='logininfo',
            name='firstname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='logininfo',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='logininfo',
            name='lastname',
            field=models.CharField(default='', max_length=100),
        ),
    ]
