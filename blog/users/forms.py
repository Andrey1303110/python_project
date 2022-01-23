from django import forms
from .models import MyUser, Message, UserOffers
from django.forms import ModelForm
from django.contrib.auth.hashers import check_password


class LoginForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget=forms.PasswordInput()

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = MyUser.objects.filter(email=email).first()
        if user is None:
            self._errors['email'] = ['Пользователя не существует']
        elif not check_password(password, user.password):
            self._errors['email'] = []
            self._errors['password'] = ['Неправильный пароль']

        return cleaned_data


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


class MessageForm(forms.ModelForm):
    text_message = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ваше соообщение'
            }
        )
    )

    class Meta:
        model = Message
        fields = ('to_message', 'text_message')


class OfferBuyForm(forms.ModelForm):
    offer_title = forms.CharField(
        label='',
        widget=forms.HiddenInput()
    )

    class Meta:
        model = UserOffers
        fields = ('offer_title',)
