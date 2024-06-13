from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', data)
#http://127.0.0.1:8000

def about(request):
    return render(request, 'main/about.html', {'title': ''})
#http://127.0.0.1:8000/about/


def contacts(request):
    return render(request, 'main/contacts.html')

