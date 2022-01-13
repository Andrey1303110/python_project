from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Имя пользователя'
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput
    )


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        help_text='Не более 150 символов',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField()
    password1 = forms.CharField(
        label='Пароль',
        help_text='Не менее 8 символов',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
