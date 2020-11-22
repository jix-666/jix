from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    """UserProfile class which has user and url image."""
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    image_url = models.CharField(max_length=100)  # image of the userprofile
