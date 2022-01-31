from django.conf import settings
from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    if request.user.is_authenticated:
        data = {
            'title': 'News page',
            'news': Articles.objects.order_by('-date')
        }
        return render(request, 'news/news_home.html', data)

    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/news_detail.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    context_object_name = 'article'
    form_class = ArticlesForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Редактирование записи'
        data['button_text'] = 'Обновить запись'
        data['script'] = 'main/js/update_news.js'
        return data


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news_delete.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Удаление записи'
        return data


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена неверно'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error,
        'title': 'Форма по добавлению статьи',
        'button_text': 'Добавить запись',
        'script': 'update_news.js'
    }
    return render(request, 'news/create.html', data)
