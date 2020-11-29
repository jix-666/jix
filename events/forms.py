import datetime

from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms
from django.forms import ModelForm

from events.models import Event


class EventForm(ModelForm):
    """A form to create an event."""

    class Meta:
        model = Event
        fields = ['title', 'description', 'category', 'appointment_date', 'image_upload']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
                   'category': forms.Select(attrs={'class': 'form-control'}),
                   'appointment_date': DateTimePickerInput(options={
                       'minDate': datetime.datetime.now().strftime('%m/%d/%Y %H:%M'),
                   }),
                   'image_upload': forms.ClearableFileInput(attrs={'class': 'form-control'}),
                   }
