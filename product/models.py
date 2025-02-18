from bs4 import BeautifulSoup
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from meta.models import ModelMeta
from slugify import slugify
from sorl.thumbnail import delete, get_thumbnail


class Type(ModelMeta, models.Model):
    title = models.CharField(
        verbose_name='Тип продукции',
        help_text='Введите ваше название типа продукции',
        max_length=150,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        help_text='Это поле опционально, вы можете его не заполнять, \
                алгоритм сгенерирует slug за вас',
    )
    description = RichTextUploadingField(
        verbose_name='Описание',
        help_text='Введите ваше описание типа продукции',
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to='uploads/img/type/%Y/%m',
        verbose_name='Изображение',
        help_text='Загрузите изображение',
        null=True,
    )
    priority = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Приоритет',
        help_text='Чем меньше число, тем выше приоритет \
                (минимальное значение — 1)',
        validators=[MinValueValidator(1)],
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )

    _metadata = {
        'title': 'title',
        'description': 'get_cleaned_description',
        'image': 'get_image_absolute_url',
        'site_name': 'Keratech',
    }

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:type_detail', args=[self.slug])

    def get_image_absolute_url(self):
        return self.photo.url

    def get_cleaned_description(self):
        if self.description:
            soup = BeautifulSoup(self.description, 'html.parser')
            return soup.get_text()
        return ''

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
        slug = slug_candidate

        while Type.objects.filter(slug=slug).exists():
            slug = slug_candidate + f'-{counter}'
            counter += 1

        self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Тип продукции'
        verbose_name_plural = 'Типы продукции'
        ordering = ['priority']


class Product(ModelMeta, models.Model):
    title = models.CharField(
        'Название продукта',
        max_length=150,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        help_text='Это поле опционально, вы можете его не заполнять, \
                алгоритм сгенерирует slug за вас.',
    )
    description = RichTextUploadingField(
        verbose_name='Описание',
        help_text='Введите ваше описание продукта',
        blank=True,
        null=True,
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
        related_name='products',
        verbose_name='Тип продукции',
        help_text='Выберете тип продукции'
    )
    priority = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Приоритет',
        help_text='Чем меньше число, тем выше приоритет \
                (минимальное значение — 1)',
        validators=[MinValueValidator(1)],
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )

    _metadata = {
        'title': 'title',
        'description': 'get_cleaned_description',
        'image': 'get_image_absolute_url',
        'site_name': 'Keratech',
    }

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.slug])

    def get_image_absolute_url(self):
        return self.photo.url

    def get_cleaned_description(self):
        if self.description:
            soup = BeautifulSoup(self.description, 'html.parser')
            return soup.get_text()
        return ''

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
        slug = slug_candidate

        while Product.objects.filter(slug=slug).exists():
            slug = slug_candidate + f'-{counter}'
            counter += 1

        self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['priority']


class ProductGallery(models.Model):
    photo = models.ImageField(
        upload_to='uploads/img/product/gallery/%Y/%m',
        verbose_name='Изображение',
        help_text='загрузите изображение',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт',
        help_text='Выберете продукт'
    )
    priority = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Приоритет',
        help_text='Чем меньше число, тем выше приоритет \
                (минимальное значение — 1)',
        validators=[MinValueValidator(1)],
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

    img_tmb.short_description = 'Изображения'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    class Meta:
        verbose_name = 'Изображение продукта'
        verbose_name_plural = 'Изображения продуктов'
        ordering = ['priority']
