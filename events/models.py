from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

CATEGORY_CHOICES = [
    ('category', 'Category'),
    ('eating', 'Eating'),
    ('sport', 'Sport'),
    ('party', 'Party'),
]


class Event(models.Model):
    """Event class which has title, description, created_at, appointment_date, image_url and attendees."""

    title = models.CharField(max_length=40)  # title of the event
    description = models.TextField(max_length=300)  # description of the event
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='category')  # category of the event
    created_at = models.DateTimeField(default=timezone.now)  # created date of the event
    appointment_date = models.DateTimeField()  # appointment date of the event
    image_url = models.CharField(max_length=100)  # image of the event
    # attendees of the event , we'll be dealing with this later
    # attendees = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE
    #
    # )
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)
