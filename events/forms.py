from django.forms import ModelForm
from events.models import Event
from django import forms


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'category', 'appointment_date', 'image_url']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.Textarea(attrs={'class': 'form-control'}),
                   'appointment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                   'image_url': forms.TextInput(attrs={'class': 'form-control'}), }
