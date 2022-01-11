from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib import messages


def login_user(request):
    data = {
        'title': 'Login Page',
        'button_text': 'sign in',
        'form': LoginForm(),
    }
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('news_home')
            else:
                messages.error(request, 'Вы ввели неверный пароль или логин!')
                return render(request, 'registration/login.html', data)
        else:
            messages.error(request, 'Поля были неверно заполнены!')
            return render(request, 'registration/login.html', data)
    else:
        return render(request, 'registration/login.html', data)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('login')
        else:
            form = UserCreationForm()
            messages.error(request, 'Ошибка регистрации!')

        data = {
            'title': 'Registration Page',
            'button_text': 'registration',
            'form': form,
        }
        return render(request, 'registration/register.html', data)
