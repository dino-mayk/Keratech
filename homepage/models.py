from django.db import models

from core.models import BaseImgModel, BaseModel
from core.validators import validate_image_aspect_ratio


def validate_image_aspect_ratio_func(image):
    validate_image_aspect_ratio(image, (16, 9))


class CarouselImg(BaseModel, BaseImgModel, models.Model):
    title = models.CharField(
        'Заголовок слайда',
        default='Заголовок слайда',
        max_length=150,
    )
    description = models.TextField(
        verbose_name='Описание',
        default='Описание',
        help_text='Введите ваше описание слайда',
    )
    TEXT_POSITION_CHOICES = [
        ('TOP', 'Вверху'),
        ('BOTTOM', 'Внизу'),
    ]
    text_position = models.CharField(
        'Расположение текста',
        max_length=10,
        choices=TEXT_POSITION_CHOICES,
        default='BOTTOM',
    )

    def __str__(self):
        return self.photo.url

    class Meta:
        verbose_name = 'Изображение карусели'
        verbose_name_plural = 'Изображения карусели'
