from django import forms


class ProfileForm(forms.Form):
    """A form to check profile."""

    user_name = forms.CharField()
    email = forms.CharField()
    profile_pic = forms.ImageField(required=False)
