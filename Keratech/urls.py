from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('homepage.urls'), name='homepage'),
    path('product/', include('product.urls'), name='product'),
    path('about/', include('about.urls'), name='about'),

    path('grappelli/', include('grappelli.urls'), name='grappelli'),
    path('tinymce/', include('tinymce.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('djeym/', include('djeym.urls', namespace='djeym')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
