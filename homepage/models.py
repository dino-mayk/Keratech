from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail

from core.validators import validate_image_aspect_ratio


def validate_image_aspect_ratio_func(image):
    validate_image_aspect_ratio(image, (16, 9))


class CarouselImg(models.Model):
    photo = models.ImageField(
        upload_to='uploads/img/carousel/%Y/%m',
        verbose_name='Изображение',
        help_text='Загрузите изображение',
        null=True,
        validators=[validate_image_aspect_ratio_func],
    )
    priority = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Приоритет',
        help_text='Чем меньше число, тем выше приоритет (0 - самый высокий)',
    )

    def __str__(self):
        return self.photo.url

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

    class Meta:
        verbose_name = 'Изображение карусели'
        verbose_name_plural = 'Изображения карусели'
        ordering = ['priority']
