from django.contrib import admin

from homepage.models import CarouselImg


@admin.register(CarouselImg)
class AdminCarouselImg(admin.ModelAdmin):
    list_display = [
        'priority',
        'img_tmb',
    ]
