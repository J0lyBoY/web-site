from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView


def news_main(request):
    news = News.objects.all()
    return render(request, 'news/news_main.html', {'news': news})


class NewsDetail(DetailView):
    model = News
    template_name = 'news/news-detail.html'
    context_object_name = 'News'


def create_news(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = NewsForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/create.html', data)
