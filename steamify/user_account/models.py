from django.db import models
from user_management.models import loginInfo
from datetime import datetime, timedelta, timezone
from django.utils import timezone

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100,)
    # Add other fields as per your requirements



class SubscribedUsers(models.Model):
    username = models.CharField(max_length=150)
    card_number = models.CharField(max_length=16)  # Assuming card numbers have 16 digits
    cardholder_name = models.CharField(max_length=100)
    expiry_date = models.CharField(max_length=5)  # Format: MM/YY
    cvv = models.CharField(max_length=4)
    subscription_date = models.DateField(default=timezone.now)  # Automatically set when a new record is added
    #subscription_expirydate = models.DateField(default=timezone.now().date() + timezone.timedelta(days=30))
    # def save(self, *args, **kwargs):
    #     # Calculate subscription_expirydate based on subscription_date plus one month
    #     if not self.subscription_expirydate:
    #         expiry_date_parts = self.expiry_date.split('/')
    #         month, year = int(expiry_date_parts[0]), int(expiry_date_parts[1])
    #         expiry_datetime = datetime(year, month, 1) + timedelta(days=31)
    #         self.subscription_expirydate = expiry_datetime.date()
    #     super().save(*args, **kwargs) # Assuming CVV has 3 or 4 digits

    def __str__(self):
        return self.cardholder_name

