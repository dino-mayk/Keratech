from django.contrib import admin
from django.contrib.auth.models import Group
from metatags.admin import MetaTagInline

from product.models import Product, ProductGallery, Type


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'img_tmb',
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'img_tmb',
    ]


@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = [
        'product',
        'img_tmb',
    ]


class CustomModelAdmin(admin.ModelAdmin):
    inlines = (MetaTagInline, )


admin.site.unregister(Group)
