from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import LoginForm, UserRegisterForm
from django.contrib import messages
from .models import MyUser


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
            user = authenticate(
                username=cleaned_data['username'],
                password=cleaned_data['password'],
            )
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
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('news_home')
        else:
            messages.error(request, 'Ошибка регистрации!')
            return redirect('register')
    else:
        data = {
            'title': 'Registration Page',
            'button_text': 'registration',
            'form': UserRegisterForm(),
        }
        return render(request, 'registration/register.html', data)


def logout_user(request):
    logout(request)
    return redirect('login')


def my_profile(request):
    data = {
        'title': 'My profile',
    }
    return render(request, 'main/profile.html', data)


def chat(request):
    users_list = MyUser.objects.all()
    data = {
        'users_list': users_list,
    }
    return render(request, 'chat/main.html', data)
