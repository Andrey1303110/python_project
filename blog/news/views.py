from django.shortcuts import render

def news_home(request):
    data = {
        'title': 'News page',
    }
    return render(request, 'news/news_home.html', data)
