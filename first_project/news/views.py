from django.shortcuts import render
from .models import News

def news_home(request):
    context = {
        'articles': News.objects.all(),
    }
    return render(request, 'news/news_home.html', context=context)
