from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            }),
            "date": DateTimeInput(attrs={
                    'autocomplete': 'on',
                    'type': 'datetime-local',
                    'class': 'form-control',
                    'placeholder': 'Дата'
                },
                format='%m/%d/%Y %H:%M')},
