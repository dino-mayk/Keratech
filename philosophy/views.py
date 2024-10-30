from django.shortcuts import render

from philosophy.models import Thought


def index(request):
    template_name = 'philosophy/index.html'
    thoughts = Thought.objects.all()

    context = {
        'title': 'Философия',
        'thoughts': thoughts,
    }

    return render(request, template_name, context)
