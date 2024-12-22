from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail


class CarouselImg(models.Model):
    title = models.CharField(
        'Заголовок слайда',
        max_length=150,
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите ваше описание слайда',
    )
    photo = models.ImageField(
        upload_to='uploads/img/carousel/%Y/%m',
        verbose_name='Изображение',
        help_text='Загрузите изображение',
        null=True,
    )

    @property
    def get_img(self):
        return get_thumbnail(
            self.photo,
            '300x300',
            crop='center',
            quality=51,
        )

    def img_tmb(self):
        if self.photo:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'Нет изображений'

    img_tmb.short_description = 'Изображения карусели'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.photo.url

    class Meta:
        verbose_name = 'Изображение карусели'
        verbose_name_plural = 'Изображения карусели'
