from django.shortcuts import render

from product.models import Type


def index(request):
    template_name = 'homepage/index.html'
    types = Type.objects.all()

    context = {
        'title': 'Главная',
        'types': types,
    }

    return render(request, template_name, context)
