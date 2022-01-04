from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    data = {
        'title': 'News page',
        'news': Articles.objects.order_by('-date')
    }
    return render(request, 'news/news_home.html', data)


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/news_detail.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/news_update.html'
    context_object_name = 'article'
    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news_delete.html'
    context_object_name = 'article'


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
        'error': error,
        'title': 'Форма по добавлению статьи'
    }
    return render(request, 'news/create.html', data)
