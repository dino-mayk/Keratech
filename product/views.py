from django.shortcuts import get_object_or_404, render

from product.models import Product, ProductGallery, Type


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


def group_images_by_products(product_images):
    products = {}

    for product_img in product_images:
        product_id = product_img.product_id

        if product_id not in products:
            products[product_id] = []

        products[product_id].append(product_img)

    return products


def type_detail(request, slug):
    template_name = 'product/type_detail.html'

    type = get_object_or_404(Type, slug=slug)

    all_products = Product.objects.all()
    all_images = ProductGallery.objects.all()

    products_for_type = None
    images_for_products = None

    # здесь требуется придумать логику функции group_products_by_types
    # и group_images_by_products дабы можно было добавлять туда
    # дополнительные опциональные условие для валидации объектов

    if len(all_products) > 0:
        products_for_type = group_products_by_types(all_products)[type]

        images_for_products = group_images_by_products(all_images)

        images_for_products = [
            x
            for x in images_for_products
            if x in products_for_type
        ]

    context = {
        'title': type.title,
        'type': type,
        'products_for_type': products_for_type,
        'images_for_products': images_for_products,
    }

    return render(request, template_name, context)


def product_list(request):
    template_name = 'product/product_list.html'

    all_products = Product.objects.all()
    all_images = ProductGallery.objects.all()

    grouped_products = group_products_by_types(all_products)
    grouped_images = group_images_by_products(all_images)

    context = {
        'title': 'Каталог',
        'grouped_products': grouped_products,
        'grouped_images': grouped_images,
    }

    return render(request, template_name, context)


def product_detail(request, slug):
    template_name = 'product/product_detail.html'

    product = get_object_or_404(Product, slug=slug)
    product_gallery = ProductGallery.objects.product_gallery(
        product_id=product.id,
    )

    context = {
        'title': product.title,
        'product': product,
        'product_gallery': product_gallery,
    }

    return render(request, template_name, context)
