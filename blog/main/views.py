from django.shortcuts import render


def index(request):
    data = {
        'title': 'Main page',
        'values': ['some', 'hello', '123'],
        'objects': {
            'cars': ['seat', 'mercedes', 'audi'],
            'age': '18',
            'hobby': 'Swimming',
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')