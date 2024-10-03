from django.contrib import admin
from django.contrib.auth.models import Group

from product.models import Product, ProductGallery


@admin.register(Product)
class AdminProducts(admin.ModelAdmin):
    list_display = [
        'title',
    ]


@admin.register(ProductGallery)
class AdminProductGallery(admin.ModelAdmin):
    list_display = [
        'item',
        'img_tmb',
    ]


admin.site.unregister(Group)
