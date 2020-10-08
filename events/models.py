from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.


class Event(models.Model):
    """Event class which has title, description, created_at, appointment_date, image_url and attendees."""

    title = models.CharField(max_length=40)  # title of the event
    description = models.TextField(max_length=300)  # description of the event
    category = models.CharField(max_length=30)  # category of the event
    created_at = models.DateTimeField(default=timezone.now())  # created date of the event
    appointment_date = models.DateTimeField()  # appointment date of the event
    image_url = models.CharField()  # image of the event
    attendees = models.ForeignKey(  # attendees of the event
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    slug = models.SlugField()
