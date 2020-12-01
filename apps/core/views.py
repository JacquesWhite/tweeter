from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout


def frontpage(request):
    return render(request, 'core/frontpage.html')


def sign_in(request):
    return render(request, 'core/login.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('frontpage')
