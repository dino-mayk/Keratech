from django.contrib import sitemaps
from django.urls import reverse

from product.models import Product, Type


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1

    def items(self):
        return [
            ('homepage:index', 'monthly'),
            ('product:product_list', 'daily'),
            ('about:index', 'yearly'),
        ]

    def location(self, item):
        return reverse(item[0])

    def changefreq(self, item):
        return item[1]


class TypeSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Type.objects.all()

    def lastmod(self, obj):
        return obj.pub_date


class ProductSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
