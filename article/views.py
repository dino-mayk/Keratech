from django.shortcuts import render

from article.models import Article


def list(request):
    template_name = 'article/list.html'
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, template_name, context)


def detail(request, pk):
    template_name = 'article/detail.html'
    article = Article.objects.get(pk=pk)

    context = {'article': article}

    return render(request, template_name, context)
