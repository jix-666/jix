from django import forms

from django.contrib.auth.models import User


class ProfileForm(forms.Form):
    """A form to check profile."""

    user_name = forms.CharField()
    first_name = forms.CharField()
    email = forms.CharField()
    profile_pic = forms.ImageField()
