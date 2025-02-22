from bs4 import BeautifulSoup
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from slugify import slugify
from sorl.thumbnail import delete, get_thumbnail


class BaseModel(models.Model):
    priority = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Приоритет',
        help_text='Чем меньше число, тем выше приоритет \
                (минимальное значение — 1)',
        validators=[MinValueValidator(1)],
    )

    class Meta:
        ordering = ['priority']
        abstract = True


class BaseImgModel(models.Model):
    photo = models.ImageField(
        upload_to='uploads/img/preview/%Y/%m',
        verbose_name='Изображение',
        help_text='Загрузите изображение',
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
        return 'Нет изображений'

    img_tmb.short_description = 'Изображение'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    class Meta:
        abstract = True


class BaseMetaModel(models.Model):
    title = models.CharField(
        'Название',
        max_length=150,
    )
    description = RichTextUploadingField(
        verbose_name='Описание',
        help_text='Введите ваше описание',
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        help_text="Это поле опционально, алгоритм сгенерирует slug за вас.",
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

    def get_image_absolute_url(self):
        return self.photo.url

    def get_cleaned_description(self, max_length=160):
        if self.description:
            soup = BeautifulSoup(self.description, "html.parser")
            text = soup.get_text().strip()
            if len(text) > max_length:
                return f"{text[:max_length]}..."
            return text
        return ""

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_candidate = slugify(self.title)
            counter = 1
            slug = slug_candidate
            while self.__class__.objects.filter(slug=slug).exists():
                slug = f"{slug_candidate}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
