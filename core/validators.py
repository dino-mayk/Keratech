from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image as PILImage


def validate_image_aspect_ratio(image, aspect_ratio):
    try:
        img = PILImage.open(image)
        width, height = img.size
        expected_ratio = aspect_ratio[0] / aspect_ratio[1]
        actual_ratio = width / height
        if abs(actual_ratio - expected_ratio) > 0.01:
            raise ValidationError(
                _(f'Изображение должно иметь соотношение сторон '
                  f'{aspect_ratio[0]}:{aspect_ratio[1]}. '
                  f'Пожалуйста, загрузите изображение с '
                  f'правильными пропорциями.'),
                params={'value': image},
            )
    except IOError:
        raise ValidationError(
            _('Не удалось открыть изображение. '
              'Убедитесь, что файл является '
              'действительным изображением.'),
            params={'value': image},
        )
