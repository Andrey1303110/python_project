from django.shortcuts import render

def news_home(request):
    data = {
        'title': 'News page',
    }
    return render(request, 'main/about.html', data)
