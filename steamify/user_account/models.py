from django.db import models
from user_management.models import loginInfo
from datetime import datetime, timedelta, timezone
from django.utils import timezone

# Create your models here.
class Video(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/', default='default_video.mp4')
    # Add other fields as per your requirements



class SubscribedUsers(models.Model):
    username = models.CharField(max_length=150)
    card_number = models.CharField(max_length=16)  # Assuming card numbers have 16 digits
    cardholder_name = models.CharField(max_length=100)
    expiry_date = models.CharField(max_length=5)  # Format: MM/YY
    cvv = models.CharField(max_length=4)
    subscription_date = models.DateField(default=timezone.now)  # Automatically set when a new record is added
    #subscription_expirydate = models.DateField(default=timezone.now().date() + timezone.timedelta(days=30))


    def __str__(self):
        return self.cardholder_name

