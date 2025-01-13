from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, render
from meta.views import Meta

from product.models import Product, ProductGallery, Type


def type_detail(request, slug):
    template_name = 'product/type_detail.html'
    type = get_object_or_404(Type, slug=slug)

    products_for_type = Product.objects.filter(type=type).prefetch_related(
        Prefetch(
            'productgallery_set', queryset=ProductGallery.objects.all(),
            to_attr='images',
        )
    )

    context = {
        'meta': type.as_meta(),
        'type': type,
        'products_for_type': products_for_type,
    }

    return render(request, template_name, context)


def product_list(request):
    template_name = 'product/product_list.html'

    protocol = request.scheme
    host = request.get_host()
    base_url = f"{protocol}://{host}"

    meta = Meta(
        title='Каталог огнеупорных и изоляционных материалов КЕРАТЕХ',
        description='Каталог огнеупорных и изоляционных материалов КЕРАТЕХ.'
        'Собственное производство огнеупорных материалов. Рассчитать стоимость'
        'изготовления установок онлайн или по телефону +79507587027.',
        keywords=[
            'КЕРАТЕХ', 'огнеупорные материалы', 'изоляционные материалы',
            'сталеразливка', 'собственное производство',
        ],
        url=request.build_absolute_uri(),
        object_type='Organization',
        site_name='Keratech',
        schemaorg_type='Organization',
        schemaorg_title='Keratech',
        use_json_ld=True,
        schema={
            'image': f'{base_url}/static/favicon/logo_text.svg',
            'url': base_url,
            'logo': f'{base_url}/static/favicon/logo_text.svg',
            'name': 'Catalog of refractory and insulating materials KERATECH.',
            'description': 'Catalog of refractory and insulating materials '
                    'KERATECH. Own production of refractory materials. '
                    'Calculate the cost of plant manufacturing online or by '
                    'phone +79507587027.',
            'email': 'keratekh@yandex.ru',
            'telephone': '+7-950-758-70-27',
        }
    )

    products = Product.objects.all().prefetch_related('productgallery_set')

    context = {
        'meta': meta,
        'products': products,
    }

    return render(request, template_name, context)


def product_detail(request, slug):
    template_name = 'product/product_detail.html'

    product = get_object_or_404(Product, slug=slug)
    product_gallery = ProductGallery.objects.filter(product=product)

    context = {
        'meta': product.as_meta(),
        'product': product,
        'product_gallery': product_gallery,
    }

    return render(request, template_name, context)
