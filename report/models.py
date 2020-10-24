# Create your models here.
from django.db import models
from events.models import Event
from django.utils import timezone

REPORT_TYPE = [
    ('', '----------'),
    ('nonworking', "Something isn't Working"),
    ('sexual_abusive', 'Sexually explicit event'),
    ('spam', 'Spam or scam'),
    ('hate_speech', 'Hate Speech'),
    ('violence', 'Violence or Harmful event'),
]


class Report(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # event class
    report_type = models.TextField(max_length=15, choices=REPORT_TYPE, default='')
    detail = models.TextField(max_length=500)  # detail of the report
    reported_at = models.DateTimeField(default=timezone.now)  # reported date of the event
    slug = models.SlugField(unique=True)


