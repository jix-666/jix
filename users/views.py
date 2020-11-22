from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import ProfileForm
from .models import UserProfile


def profile_page(request, username):
    """Log user into the site."""
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        messages.warning(request, 'User not found.')
        return redirect('events:feed')
    user_profile = UserProfile.objects.get(user=user)
    if user_profile.user == request.user and request.user.is_authenticated:
        profile_form = ProfileForm(initial={
            'user_name': user_profile.user.username,
            'first_name': user_profile.user.first_name,
            'email': user_profile.user.email,
            'profile_pic': user_profile.user.userprofile.profile_picture
        })
        if request.method == 'POST':
            profile_form = ProfileForm(request.POST, request.FILES)

            if profile_form.is_valid():
                if user_profile.user == request.user and request.user.is_authenticated:
                    user_username = profile_form.cleaned_data['user_name']
                    user_profile.user.username = user_username
                    user_profile.user.email = profile_form.cleaned_data['email']
                    user_profile.user.first_name = profile_form.cleaned_data['first_name']
                    user_profile.profile_picture = profile_form.cleaned_data['profile_pic']
                    user_profile.save()
                    messages.info(request, f'{username} profile was updated.')
                    return redirect('users:profile', username)
                else:
                    messages.warning(request, f'You can not edit {username} profile.')
    else:
        messages.warning(request, f'You can not edit {username} profile.')
        return redirect('events:feed')

    return render(request, 'users/profile.html',
                  {'user_profile': user_profile, 'profile_form': profile_form})
