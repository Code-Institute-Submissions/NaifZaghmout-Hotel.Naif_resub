
"""
Database Models
"""
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Hotels(models.Model):
    """
    Hotels Info
    Hotel Name, Owner Name, Location, State Country
    """

    hotel_name = models.CharField(max_length=30, default="Naif")
    hotel_owner = models.CharField(max_length=20)
    hotel_location = models.CharField(max_length=50)
    hotel_state = models.CharField(max_length=50, default="Dubai")
    hotel_country = models.CharField(max_length=50, default="UAE")

    def __str__(self):
        return self.hotel_name