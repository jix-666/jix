# Create your models here.
from django.db import models
from django.utils import timezone

from events.models import Event

REPORT_TYPE = [
    ('', '----------'),
    ('non-working', "Something isn't Working"),
    ('sexual-abusive', 'Sexually explicit event'),
    ('spam', 'Spam or scam'),
    ('hate-speech', 'Hate Speech'),
    ('violence', 'Violence or Harmful event'),
]


class Report(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # event class
    report_type = models.CharField(max_length=15, choices=REPORT_TYPE, default='')
    detail = models.TextField(max_length=500)  # detail of the report
    reported_at = models.DateTimeField(default=timezone.now)  # reported date of the event
