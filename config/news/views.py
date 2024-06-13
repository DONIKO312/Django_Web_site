from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from .forms import NewsForm

def news_home(request):
    news = News.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неправильно заполнена'

    form = NewsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)

def news_list(request):
    news = News.objects.all()
    return render(request, 'news/news_list.html', {'news': news})

def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news_item})

def news_create(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news_item = form.save(commit=False)
            news_item.save()
            return redirect('news_detail', pk=news_item.pk)
    else:
        form = NewsForm()
    return render(request, 'news/news_edit.html', {'form': form})

def news_update(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=news_item)
        if form.is_valid():
            news_item = form.save(commit=False)
            news_item.save()
            return redirect('news_detail', pk=news_item.pk)
    else:
        form = NewsForm(instance=news_item)
    return render(request, 'news/news_edit.html', {'form': form})

def news_delete(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    news_item.delete()
    return redirect('news_list')
