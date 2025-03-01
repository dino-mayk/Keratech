from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from .sitemaps import (PageSitemap, ProductSitemap, StaticViewSitemap,
                       TypeSitemap)

sitemaps = {
    'static': StaticViewSitemap,
    'types': TypeSitemap,
    'products': ProductSitemap,
    'pages': PageSitemap,
}

handler404 = 'core.views.error_404'

urlpatterns = [
    path(
        'admin/',
        admin.site.urls,
    ),

    path(
        'chaining/',
        include('smart_selects.urls'),
    ),
    path(
        'ckeditor/',
        include('ckeditor_uploader.urls'),
    ),
    path(
        'djeym/',
        include('djeym.urls', namespace='djeym'),
    ),

    path(
        '',
        include('homepage.urls'),
        name='homepage',
    ),
    path(
        'product/',
        include('product.urls'),
        name='product',
    ),
    path(
        'feedback/',
        include('feedback.urls'),
        name='feedback',
    ),
    path(
        'about/', include('about.urls'),
        name='about',
    ),
    path(
        '',
        include('page.urls'),
        name='page',
    ),

    path(
        '', include('core.urls'),
        name='core',
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
