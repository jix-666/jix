from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register_page(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account for {user} was created')
            return redirect('login')
        else:
            messages.info(request, 'Username or Password is incorrect.')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('events:feed')
        else:
            messages.warning(request, 'Username or Password is incorrect.')

    context = {}
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')