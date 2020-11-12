from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import UserForm


# Create your views here.
def register_page(request):
    """Register user account for the site."""
    if request.user.is_authenticated:
        return redirect('events:feed')
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account for {user} was created')
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_page(request):
    """Log user into the site."""
    if request.user.is_authenticated:
        return redirect('events:feed')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('events:feed')
        else:
            messages.warning(request, 'Username or Password is incorrect.')

    return render(request, 'accounts/login.html')


def logout_user(request):
    """Log user out of the site."""
    logout(request)
    return redirect('login')
