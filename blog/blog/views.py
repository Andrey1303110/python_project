from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        error: {''}
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('news_home')
            else:
                error: {
                    'Your account has disabled!'
                }
        else:
            error: {
                'Invalid login!'
            }
    else:
        data = {
            'title': 'Login Page',
            'button_text': 'sign in',
            'form': LoginForm(),
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
