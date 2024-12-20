
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail
from transliterate import slugify

from core.validators import validate_image_aspect_ratio
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
        help_text="""Это поле опционально, вы можете его не заполнять,
                 алгоритм сгенерирует slug за вас.""",
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
        validators=[lambda image: validate_image_aspect_ratio(image, (4, 3))],
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )

    @property
    def get_img(self):
        return get_thumbnail(
            self.photo,
            '320x240',
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

        if slug_candidate is None:
            slug_candidate = 'obj'

        counter = 1
        slug = slug_candidate

        while Type.objects.filter(slug=slug).exists():
            slug = slug_candidate + f"-{counter}"
            counter += 1

        self.slug = slug
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
        help_text="""Это поле опционально, вы можете его не заполнять,
                 алгоритм сгенерирует slug за вас.""",
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
        validators=[lambda image: validate_image_aspect_ratio(image, (4, 3))],
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        verbose_name="Тип продукции",
        help_text='Выберете тип продукции'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )

    @property
    def get_img(self):
        return get_thumbnail(
            self.photo,
            '320x240',
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

        if slug_candidate is None:
            slug_candidate = 'obj'

        counter = 1
        slug = slug_candidate

        while Product.objects.filter(slug=slug).exists():
            slug = slug_candidate + f"-{counter}"
            counter += 1

        self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.slug])

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductGallery(models.Model):
    photo = models.ImageField(
        upload_to='uploads/img/product/gallery/%Y/%m',
        verbose_name="Изображение",
        help_text='загрузите изображение',
        validators=[lambda image: validate_image_aspect_ratio(image, (4, 3))],
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
        return get_thumbnail(
            self.photo,
            '320x240',
            crop='center',
            quality=51,
        )

    def img_tmb(self):
        if self.photo:
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
        return self.photo.url

    class Meta:
        verbose_name = "Изображение продукта"
        verbose_name_plural = "Изображения продуктов"
