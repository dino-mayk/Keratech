from django.shortcuts import render


def index(request):
    template_name = 'map/index.html'

    context = {
        'title': 'Мы на картах',
    }

    return render(request, template_name, context)
