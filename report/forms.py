from django import forms
from django.forms import ModelForm

from .models import Report


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['report_type', 'detail']
        widgets = {'detail': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
                   'report_type': forms.Select(attrs={'class': 'form-control'}), }
