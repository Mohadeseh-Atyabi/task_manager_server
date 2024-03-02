from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm
from django.contrib import messages


def login_user(req):
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(req, username=username, password=password)
            if user:
                login(req, user)
                return redirect('show task')
            else:
                messages.error(req, 'User not found, try again')

    else:
        form = LoginForm()

    return render(req, 'login.html', {'form': form})
