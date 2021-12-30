from django.shortcuts import render
from .models import Articles

def news_home(request):
    data = {
        'title': 'News page',
        'news': Articles.objects.all()
    }
    return render(request, 'news/news_home.html', data)
