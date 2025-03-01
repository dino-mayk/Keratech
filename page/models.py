from django.db import models
from django.urls import reverse

from core.models import BaseMetaModel


class Page(BaseMetaModel, models.Model):
    def get_absolute_url(self):
        return reverse('page:page_detail', args=[self.slug])

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
