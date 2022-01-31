from .models import Articles
from django.forms import ModelForm


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'date', 'full_text', 'image']
