from django.db.models import QuerySet
from django.shortcuts import render

from product.models import Product


def group_products_by_type(products: QuerySet) -> dict:
    grouped_products = {}
    for product in products:
        product_type = product.type
        if product_type not in grouped_products:
            grouped_products[product_type] = []
            grouped_products[product_type].append(product)
    return grouped_products


def list(request):
    template_name = 'product/list.html'

    all_products = Product.objects.all()

    grouped_products = group_products_by_type(all_products)

    print(grouped_products)

    context = {
        'products': grouped_products,
    }
    return render(request, template_name, context)


def detail(request, pk):
    template_name = 'product/detail.html'
    product = Product.objects.get(pk=pk)

    context = {'product': product}

    return render(request, template_name, context)
