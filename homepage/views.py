from django.shortcuts import render
from meta.views import Meta

from homepage.models import CarouselImg
from product.models import Type


def index(request):
    template_name = 'homepage/index.html'
    meta = Meta(
        title='Поставщик огнеупорных и изоляционных материалов КЕРАТЕХ',
        description='Огнеупорные и изоляционные материалы КЕРАТЕХ с доставкой '
        'по РФ. Вся продукция соответствует международным стандартам. Качество'
        ' и надежность. Современные огнеупорные технологии для повышения '
        'эффективности и конкурентоспособности. Для заказа огнеупорных '
        'материалов звоните +79507587027.',
        keywords=[
            'Огнеупорные материалы', 'изоляционные материалы',
            'КЕРАТЕХ', 'доставка по РФ', 'международные стандарты',
            'качество', 'надежность', 'современные технологии',
        ],
    )

    carousel_imgs = CarouselImg.objects.all()
    types = Type.objects.all()

    context = {
        'meta': meta,
        'types': types,
        'carousel_imgs': carousel_imgs,
    }

    return render(request, template_name, context)
