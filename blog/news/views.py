from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


def news_home(request):
    data = {
        'title': 'News page',
        'news': Articles.objects.order_by('-date')
    }
    return render(request, 'news/news_home.html', data)


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена неверно'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
