from django.shortcuts import render

from product.models import Product, ProductGallery


def group_products_by_types(products):
    types = {}

    for product in products:
        if product.type in types:
            product_list = types[product.type]
            product_list.append(product)
            types[product.type] = product_list
        else:
            types[product.type] = [product]

    return types


def list(request):
    template_name = 'product/list.html'
    all_products = Product.objects.all()
    grouped_products = group_products_by_types(all_products)

    context = {
        'grouped_products': grouped_products,
    }

    return render(request, template_name, context)


def detail(request, pk):
    template_name = 'product/detail.html'
    product = Product.objects.get(pk=pk)
    product_gallery = ProductGallery.objects.product_gallery(item_id=pk)

    context = {
        'product': product,
        'product_gallery': product_gallery,
    }

    return render(request, template_name, context)
