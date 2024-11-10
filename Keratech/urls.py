from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from .sitemaps import ProductSitemap, StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
}

urlpatterns = [
    path(
        'admin/',
        admin.site.urls,
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
        'philosophy/',
        include('philosophy.urls'),
        name='philosophy',
    ),
    # path(
    #     'map/',
    #     include('map.urls'),
    #     name='map',
    # ),

    # path(
    #     'ckeditor/',
    #     include('ckeditor_uploader.urls'),
    # ),
    # path(
    #     'djeym/',
    #     include('djeym.urls', namespace='djeym'),
    # ),

    re_path(
        r'^(?P<path>.*)$',
        lambda request,
        path: redirect('/', permanent=True),
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
