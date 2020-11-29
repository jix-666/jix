from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import ProfileForm
from .models import UserProfile
from events.models import Attendee


def profile_page(request, username):
    """Log user into the site."""
    joined_event = []
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        messages.warning(request, 'User not found.')
        return redirect('events:feed')
    user_profile = UserProfile.objects.get(user=user)
    user_attendee = Attendee.objects.filter(user=user).all()
    for user in user_attendee:
        joined_event.append(user.event)
    profile_form = ProfileForm(initial={
        'user_name': user_profile.user.username,
        'first_name': user_profile.user.first_name,
        'email': user_profile.user.email,
        'profile_pic': user_profile.profile_picture
    })
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            if user_profile.user == request.user and request.user.is_authenticated:
                if profile_form.cleaned_data['profile_pic']:
                    user_profile.profile_picture = profile_form.cleaned_data['profile_pic']
                user_username = profile_form.cleaned_data['user_name']
                user_profile.user.username = user_username
                user_profile.user.email = profile_form.cleaned_data['email']
                user_profile.user.save()
                user_profile.save()
                messages.info(request, f'{user_username} profile was updated.')
                return redirect('events:feed')
            else:
                messages.warning(request, f'You can not edit {user_profile} profile.')
    return render(request, 'users/profile.html',
                  {'user_profile': user_profile, 'profile_form': profile_form, 'joined_event': joined_event})
