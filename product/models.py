from django.db import models
from django.urls import reverse
from meta.models import ModelMeta

from core.models import BaseImgModel, BaseMetaModel, BaseModel


class Type(BaseModel, BaseImgModel, BaseMetaModel, ModelMeta, models.Model):
    def get_absolute_url(self):
        return reverse('product:type_detail', args=[self.slug])

    class Meta:
        verbose_name = 'Тип продукции'
        verbose_name_plural = 'Типы продукции'


class Product(BaseModel, BaseImgModel, BaseMetaModel, ModelMeta, models.Model):
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Тип продукции',
        help_text='Выберете тип продукции'
    )

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.slug])

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductGallery(BaseModel, BaseImgModel, models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт',
        help_text='Выберете продукт'
    )

    def __str__(self):
        return self.photo.url

    class Meta:
        verbose_name = 'Изображение продукта'
        verbose_name_plural = 'Изображения продуктов'
