from django.shortcuts import render

from product.models import Product


def list(request):
    template_name = 'product/list.html'
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, template_name, context)


def detail(request, pk):
    template_name = 'product/detail.html'
    product = Product.objects.get(pk=pk)

    context = {'product': product}

    return render(request, template_name, context)
