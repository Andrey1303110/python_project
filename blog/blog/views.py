from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def login(request):
    form = UserCreationForm()
    data = {
        'title': 'Login Page',
        'button_text': 'sign in',
        'form': form,
    }
    return render(request, 'registration/login.html', data)


def register(request):
    form = UserCreationForm()
    data = {
        'title': 'Registration Page',
        'button_text': 'registration',
        'form': form,
    }
    return render(request, 'registration/register.html', data)
