from django.shortcuts import render


def index(request):
    template_name = 'about/index.html'

    context = {
        'title': 'Связаться с нами',
    }

    return render(request, template_name, context)
