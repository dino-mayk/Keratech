from django.shortcuts import render

from homepage.models import CarouselImg
from product.models import Type


def index(request):
    template_name = 'homepage/index.html'
    carousel_imgs = CarouselImg.objects.all()
    types = Type.objects.all()

    context = {
        'title': 'Главная',
        'types': types,
        'carousel_imgs': carousel_imgs,
    }

    return render(request, template_name, context)
