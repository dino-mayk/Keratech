from bs4 import BeautifulSoup
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from meta.models import ModelMeta
from slugify import slugify
from sorl.thumbnail import delete, get_thumbnail
from tinymce.models import HTMLField


class Type(ModelMeta, models.Model):
    title = models.CharField(
        verbose_name='Тип продукции',
        help_text='Введите ваше название типа продукции',
        max_length=150,
    )
    title_en = models.CharField(
        verbose_name='Тип продукции на английском',
        help_text='Введите ваше название типа продукции на английском',
        max_length=150,
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        help_text="""Это поле опционально, вы можете его не заполнять,
                 алгоритм сгенерирует slug за вас""",
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите ваше описание типа продукции',
        blank=True,
        null=True,
    )
    description_en = models.TextField(
        verbose_name='Описание на английском',
        help_text='Введите ваше описание типа продукции на английском',
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to='uploads/img/type/%Y/%m',
        verbose_name='Изображение',
        help_text='Загрузите изображение',
        null=True,
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )

    _metadata = {
        'title': 'title',
        'description': 'description',
        'site_name': 'Keratech',
        'schemaorg_type': 'Organization',
        'schemaorg_title': 'Keratech',
        'use_json_ld': True,
    }

    _schema = {
        'url': 'get_absolute_url',
        'image': 'get_image_absolute_url',
        'name': 'title_en',
        'headline': 'title_en',
        'description': 'description_en',
        'articleBody': 'description_en',
        'datePublished': 'pub_date',
        'publisher': 'Keratech',
    }

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:type_detail', args=[self.slug])

    def get_image_absolute_url(self):
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
            slug = slug_candidate + f"-{counter}"
            counter += 1

        self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Тип продукции'
        verbose_name_plural = 'Типы продукции'


class Product(ModelMeta, models.Model):
    title = models.CharField(
        'Название продукта',
        max_length=150,
    )
    title_en = models.CharField(
        verbose_name='Название продукта на английском',
        help_text='Введите ваше название продукта на английском',
        max_length=150,
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        help_text="""Это поле опционально, вы можете его не заполнять,
                 алгоритм сгенерирует slug за вас.""",
    )
    description = HTMLField(
        verbose_name='Описание',
        help_text='Введите ваше описание продукта',
        blank=True,
        null=True,
    )
    description_en = models.TextField(
        verbose_name='Описание на английском',
        help_text='Введите ваше описание продукта на английском',
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
        verbose_name="Тип продукции",
        help_text='Выберете тип продукции'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )

    _metadata = {
        'title': 'title',
        'description': 'description',
        'site_name': 'Keratech',
        'schemaorg_type': 'Organization',
        'schemaorg_title': 'Keratech',
        'use_json_ld': True,
    }

    _schema = {
        'url': 'get_absolute_url',
        'image': 'get_image_absolute_url',
        'name': 'title_en',
        'headline': 'title_en',
        'description': 'description_en',
        'articleBody': 'description_en',
        'datePublished': 'pub_date',
        'publisher': 'Keratech',
    }

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.slug])

    def get_image_absolute_url(self):
        return self.photo.url

    def get_cleaned_description(self):
        if self.description:
            soup = BeautifulSoup(self.description, "html.parser")
            return soup.get_text()
        return ""

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
            slug = slug_candidate + f"-{counter}"
            counter += 1

        self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductGallery(models.Model):
    photo = models.ImageField(
        upload_to='uploads/img/product/gallery/%Y/%m',
        verbose_name="Изображение",
        help_text='загрузите изображение',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        help_text='Выберете продукт'
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
        verbose_name = "Изображение продукта"
        verbose_name_plural = "Изображения продуктов"
