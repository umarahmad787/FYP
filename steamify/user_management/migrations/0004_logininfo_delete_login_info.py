# Generated by Django 4.2.2 on 2023-07-05 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0003_rename_students_login_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='loginInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='login_info',
        ),
    ]
