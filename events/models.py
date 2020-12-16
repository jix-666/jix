from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from datetime import datetime

# Create your models here.

CATEGORY_CHOICES = [
    ('', '----------'),
    ('eating', 'Eating'),
    ('sport', 'Sport'),
    ('party', 'Party'),
    ('technology', 'Technology'),
    ('movies', 'Movies'),
    ('crafts', 'Crafts'),
    ('business', 'Business'),
    ('movements', 'Movements'),
    ('education', 'Education')
]


class Event(models.Model):
    """Event class which has title, description, created_at, appointment_date, image_url and attendees."""

    title = models.CharField(max_length=40)  # title of the event
    description = models.TextField(max_length=500)  # description of the event
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default='')  # category of the event
    created_at = models.DateTimeField(default=timezone.now)  # created date of the event
    appointment_date = models.DateTimeField()  # appointment date of the event
    image_upload = models.ImageField(upload_to='images/')  # image of the event
    slug = models.SlugField(unique=True, allow_unicode=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)

    def __str__(self):
        """Return a  string representation of the Event object."""
        return self.title

    def save(self, *args, **kwargs):
        """Save the slug of the Event object."""
        self.slug = self.slug or slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def is_outdated(self):
        return self.appointment_date < timezone.now()

    def is_hot(self):
        return self.attendee_set.count() >= 20


class Attendee(models.Model):
    """An Attendee model.

    Each Choice is associated with Event and a User.

    """

    event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
