from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now())
    appointment_date = models.DateTimeField()
    image_url = models.CharField()
    attendees = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    slug = models.SlugField()
