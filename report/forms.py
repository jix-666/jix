from django import forms
from django.forms import ModelForm

from .models import Report


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['event', 'report_type', 'detail']
        widgets = {'event': forms.Select(attrs={'class': 'form-control'}),
                   'detail': forms.Textarea(attrs={'class': 'form-control'}),
                   'report_type': forms.Select(attrs={'class': 'form-control'}), }
