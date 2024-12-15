from django.shortcuts import render

from product.models import Type, Product, ProductGallery


def group_all_products_by_types():
    all_products = Product.objects.all()
    types = {}

    for product in all_products:
        if product.type in types:
            product_list = types[product.type]
            product_list.append(product)
            types[product.type] = product_list
        else:
            types[product.type] = [product]

    return types


def show_products_for_type(type):
    grouped_products = group_all_products_by_types()

    return grouped_products[type]


def type_detail(request, pk):
    template_name = 'product/type_detail.html'
    type = Type.objects.get(pk=pk)
    products_for_type = show_products_for_type(type)

    context = {
        'title': type.title,
        'type': type,
        'products_for_type': products_for_type,
    }

    return render(request, template_name, context)


def product_list(request):
    template_name = 'product/product_list.html'
    grouped_products = group_all_products_by_types()

    context = {
        'title': 'Каталог',
        'grouped_products': grouped_products,
    }

    return render(request, template_name, context)


def product_detail(request, pk):
    template_name = 'product/product_detail.html'
    product = Product.objects.get(pk=pk)
    product_gallery = ProductGallery.objects.product_gallery(item_id=pk)

    context = {
        'title': product.title,
        'product': product,
        'product_gallery': product_gallery,
    }

    return render(request, template_name, context)
