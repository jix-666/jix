from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        widgets = {'username': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}, ),
                   'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                   'email': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
                   'password1': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
                   'password2': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}), }
