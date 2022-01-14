from django import forms
from .models import MyUser
from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.EmailField(
        label='Email'
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput
    )


class UserRegisterForm(ModelForm):
    email = forms.EmailField(
        label='Email',
        help_text='Не более 150 символов',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    fio = forms.CharField(
        label='ФИО',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    telegram = forms.CharField(
        label='Telegram',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    password1 = forms.CharField(
        label='Пароль',
        help_text='Не менее 8 символов',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    password2 = forms.CharField(
        label='Пароль',
        help_text='Повторите введённый ранее пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = MyUser
        fields = ('email', 'fio', 'telegram', 'password1', 'password2')
