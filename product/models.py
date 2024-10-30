from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail

from product.managers import ProductGalleryManager


class Type(models.Model):
    title = models.CharField(
        'Тип продукции',
        max_length=150,
    )
    description = models.TextField(
        verbose_name='описание',
        help_text='Введите ваше описание типа продукции',
    )
    photo = models.ImageField(
        upload_to='uploads/img/type/%Y/%m',
        verbose_name='изображение',
        help_text='Загрузите изображение',
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип продукции'
        verbose_name_plural = 'Типы продукции'


class Product(models.Model):
    title = models.CharField(
        'Название продукта',
        max_length=150,
    )
    description = models.TextField(
        verbose_name='описание',
        help_text='Введите ваше описание продукта',
    )
    photo = models.ImageField(
        upload_to='uploads/img/product/preview/%Y/%m',
        verbose_name='изображение',
        help_text='Загрузите изображение',
        null=True,
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        verbose_name="Тип продукции",
        help_text='выберете тип продукции'
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

    img_tmb.short_description = 'Изображение'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductGallery(models.Model):
    upload = models.ImageField(
        upload_to='uploads/img/product/gallery/%Y/%m',
        verbose_name="изображение",
        help_text='загрузите изображение'
    )
    item = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="продукт",
        help_text='выберете продукт'
    )
    objects = ProductGalleryManager()

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    def img_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'нет изображений'

    img_tmb.short_description = 'изображения'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.upload.url

    class Meta:
        verbose_name = "изображение продукта"
        verbose_name_plural = "изображения продуктов"
