from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail
from transliterate import slugify

from product.managers import ProductGalleryManager


class Type(models.Model):
    title = models.CharField(
        'Тип продукции',
        max_length=150,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите ваше описание типа продукции',
    )
    photo = models.ImageField(
        upload_to='uploads/img/type/%Y/%m',
        verbose_name='Изображение',
        help_text='Загрузите изображение',
        null=True,
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def save(self, *args, **kwargs):
        slug_candidate = slugify(self.title)
        counter = 1

        while Type.objects.filter(slug=slug_candidate).exists():
            slug_candidate = slugify(self.title) + f"-{counter}"
            counter += 1

        self.slug = slug_candidate
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:type_detail', args=[self.slug])

    class Meta:
        verbose_name = 'Тип продукции'
        verbose_name_plural = 'Типы продукции'


class Product(models.Model):
    title = models.CharField(
        'Название продукта',
        max_length=150,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите ваше описание продукта',
    )
    photo = models.ImageField(
        upload_to='uploads/img/product/preview/%Y/%m',
        verbose_name='Изображение',
        help_text='Загрузите изображение',
        null=True,
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        verbose_name="Тип продукции",
        help_text='Выберете тип продукции'
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

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

    img_tmb.short_description = 'Изображение'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def save(self, *args, **kwargs):
        slug_candidate = slugify(self.title)
        counter = 1

        while Product.objects.filter(slug=slug_candidate).exists():
            slug_candidate = slugify(self.title) + f"-{counter}"
            counter += 1

        self.slug = slug_candidate
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.slug])

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductGallery(models.Model):
    upload = models.ImageField(
        upload_to='uploads/img/product/gallery/%Y/%m',
        verbose_name="Изображение",
        help_text='загрузите изображение'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        help_text='Выберете продукт'
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
        return 'Нет изображений'

    img_tmb.short_description = 'Изображения'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.upload.url

    class Meta:
        verbose_name = "Изображение продукта"
        verbose_name_plural = "Изображения продуктов"
