from django.shortcuts import render

from homepage.models import CarouselImg
from product.models import Type


def index(request):
    template_name = 'homepage/index.html'

    carousel_imgs = CarouselImg.objects.all()
    if len(carousel_imgs) > 0:
        carousel_img_active = carousel_imgs[0]
    else:
        carousel_img_active = None
    carousel_imgs = carousel_imgs[1::]

    types = Type.objects.all()

    context = {
        'title': 'Главная',
        'types': types,
        'carousel_img_active': carousel_img_active,
        'carousel_imgs': carousel_imgs,
    }

    return render(request, template_name, context)
