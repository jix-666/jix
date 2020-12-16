from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    """UserProfile class which has user and profile picture."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiles/', default='user-icon.png',
                                        blank=True)  # image of the userprofile
