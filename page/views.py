from django.shortcuts import get_object_or_404, render

from .models import Page


def page_detail(request, slug):
    template_name = 'page/page_detail.html'

    page = get_object_or_404(Page, slug=slug)

    context = {
        'meta': page.as_meta(),
        'page': page,
    }

    return render(request, template_name, context)
