from django.contrib import admin

from product.models import Product


@admin.register(Product)
class AdminProducts(admin.ModelAdmin):
    list_display = [
        'title',
    ]
