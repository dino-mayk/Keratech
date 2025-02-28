from ckeditor_uploader.fields import RichTextUploadingField

from core.models import SingletonModel


class PolicyPage(SingletonModel):
    content = RichTextUploadingField(
        verbose_name='Контент',
    )

    class Meta:
        verbose_name = 'Политика в отношении обработки персональных данных'
        verbose_name_plural = 'О политике в отношении \
                                обработки персональных данных'
