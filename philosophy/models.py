from django.db import models


class Thought(models.Model):
    title = models.CharField(
        'Введите заголовок мысли',
        max_length=150,
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите текст',
    )
    photo = models.ImageField(
        upload_to='uploads/img/thought/%Y/%m',
        verbose_name='Изображение',
        help_text='Загрузите изображение',
        null=True,
    )

    def __str__(self):
        return f"Мысль №{self.id}"

    class Meta:
        verbose_name = 'Мысль'
        verbose_name_plural = 'Мысли'
