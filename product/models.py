from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail
from tinymce.models import HTMLField


class Product(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=150,
    )
    text = HTMLField(
        verbose_name='описание',
        help_text='Введите ваше описание продукта',
    )

    photo = models.ImageField(
        upload_to='uploads/preview/%Y/%m',
        verbose_name='картинка',
        help_text='Загрузите картинку',
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
        return 'нет изображений'

    img_tmb.short_description = 'Превьюшка'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
