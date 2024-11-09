from django.contrib import sitemaps
from django.urls import reverse

from product.models import Product


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = "daily"

    def items(self):
        return [
            'homepage:index',
            'product:list',
            'philosophy:index',
        ]

    def location(self, item):
        return reverse(item)


class ProductSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
