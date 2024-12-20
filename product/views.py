from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, render

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
        'title': type.title,
        'type': type,
        'products_for_type': products_for_type,
    }

    return render(request, template_name, context)


def product_list(request):
    template_name = 'product/product_list.html'
    products = Product.objects.all().prefetch_related('productgallery_set')

    context = {
        'title': 'Каталог',
        'products': products,
    }

    return render(request, template_name, context)


def product_detail(request, slug):
    template_name = 'product/product_detail.html'

    product = get_object_or_404(Product, slug=slug)
    product_gallery = ProductGallery.objects.filter(product=product)

    context = {
        'title': product.title,
        'product': product,
        'product_gallery': product_gallery,
    }

    return render(request, template_name, context)
