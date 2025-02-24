from django.shortcuts import render
from meta.views import Meta

from homepage.models import CarouselImg
from product.models import Type


def index(request):
    template_name = 'homepage/index.html'

    protocol = request.scheme
    host = request.get_host()
    base_url = f'{protocol}://{host}'

    meta = Meta(
        title='Производитель огнеупорных и изоляционных материалов КЕРАТЕХ',
        description='Огнеупорные и изоляционные материалы КЕРАТЕХ с доставкой '
        'по РФ. Вся продукция соответствует международным стандартам. Качество'
        ' и надежность. Современные огнеупорные технологии для повышения '
        'эффективности и конкурентоспособности. Для заказа огнеупорных '
        'материалов звоните +79507587027.',
        keywords=[
            'КЕРАТЕХ', 'огнеупорные материалы', 'изоляционные материалы',
            'сталеразливка', 'доставка по РФ', 'международные стандарты',
            'качество', 'надежность', 'современные технологии',
        ],
        url=request.build_absolute_uri(),
        object_type='Organization',
        site_name='Keratech',
        schemaorg_type='Organization',
        schemaorg_title='Keratech',
        use_json_ld=True,
        schema={
            '@context': 'https://schema.org',
            '@type': 'Organization',
            'image': f'{base_url}/static/favicon/logo_text.svg',
            'url': base_url,
            'logo': f'{base_url}/static/favicon/logo_text.svg',
            'name': 'Supplier of refractory and insulating materials '
                    'KERATECH.',
            'description': 'Fireproof and insulating materials KERATECH with '
                    'delivery in Russia. All products meet international '
                    'standards. Quality and reliability. Modern refractory '
                    'technologies to increase efficiency and competitiveness. '
                    'To order refractory materials call +79507587027.',
            'email': 'keratekh@yandex.ru',
            'telephone': '+7-950-758-70-27',
        }
    )

    carousel_imgs = CarouselImg.objects.all()
    types = Type.objects.all()

    context = {
        'meta': meta,
        'types': types,
        'carousel_imgs': carousel_imgs,
    }

    return render(request, template_name, context)
