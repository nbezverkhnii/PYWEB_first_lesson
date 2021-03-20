from django.shortcuts import render
from blog.models import Article


def index(request):
    context = {
        'articles': Article.objects.all(),
    }
    return render(request, 'start/start.html', context=context)
