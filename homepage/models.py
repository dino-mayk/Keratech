from django.db import models

from core.models import BaseImgModel, BaseModel
from core.validators import validate_image_aspect_ratio


def validate_image_aspect_ratio_func(image):
    validate_image_aspect_ratio(image, (16, 9))


class CarouselImg(BaseModel, BaseImgModel, models.Model):
    def __str__(self):
        return self.photo.url

    class Meta:
        verbose_name = 'Изображение карусели'
        verbose_name_plural = 'Изображения карусели'
