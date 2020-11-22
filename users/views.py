from django.contrib.auth.models import User
from django.shortcuts import render


def profile_page(request, username):
    """Log user into the site."""
    if request.user.is_authenticated:
        user = User.objects.get(username=username)
        return render(request, 'users/profile.html', {'user': user})
