from django.contrib import admin
from django.contrib.auth.models import Group

from product.models import Product, ProductGallery, Type


@admin.register(Type)
class AdminType(admin.ModelAdmin):
    list_display = [
        'title',
    ]


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
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
