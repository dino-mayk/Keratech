from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('homepage.urls'), name='homepage'),
    path('product/', include('product.urls'), name='product'),
    path('philosophy/', include('philosophy.urls'), name='philosophy'),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="main/robots.txt",
            content_type="text/plain",
        )
    ),

    # path('map/', include('map.urls'), name='map'),

    # path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('djeym/', include('djeym.urls', namespace='djeym')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
