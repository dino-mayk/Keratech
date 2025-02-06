from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic.base import TemplateView

from .sitemaps import ProductSitemap, StaticViewSitemap, TypeSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'types': TypeSitemap,
    'products': ProductSitemap,
}

handler404 = 'core.views.error_404'

urlpatterns = [
    path(
        'admin/',
        admin.site.urls,
    ),

    path(
        'froala_editor/',
        include('froala_editor.urls'),
    ),

    path(
        '',
        include('homepage.urls'), name='homepage',
    ),
    path(
        'product/',
        include('product.urls'), name='product',
    ),

    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="main/robots.txt",
            content_type="text/plain",
        )
    ),
    path(
        'sitemap.xml',
        sitemap, {'sitemaps': sitemaps},
    )
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
