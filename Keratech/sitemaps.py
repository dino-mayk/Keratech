from django.contrib import sitemaps
from django.urls import reverse

from product.models import Product, Type


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = "daily"

    def items(self):
        return [
            'homepage:index',
            'product:product_list',
        ]

    def location(self, item):
        return reverse(item)


class TypeSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return Type.objects.all()

    def lastmod(self, obj):
        return obj.pub_date


class ProductSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
