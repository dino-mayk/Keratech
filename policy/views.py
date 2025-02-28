from django.shortcuts import render
from meta.views import Meta

from .models import PolicyPage


def index(request):
    template_name = 'policy/index.html'

    protocol = request.scheme
    host = request.get_host()
    base_url = f'{protocol}://{host}'

    meta = Meta(
        title='Политика в отношении обработки персональных данных | КЕРАТЕХ',
        description='Политика компании КЕРАТЕХ в отношении обработки '
                    'персональных данных. '
                    'Информация о сборе, использовании '
                    'и защите данных пользователей.',
        keywords=[
            'КЕРАТЕХ', 'политика конфиденциальности', 'персональные данные',
            'защита информации', 'правовая информация',
            'огнеупорные материалы', 'изоляционные материалы',
            'обработка данных',
        ],
        url=request.build_absolute_uri(),
        object_type='Organization',
        site_name='Keratech',
        schemaorg_type='Organization',
        schemaorg_title='Keratech Contacts',
        use_json_ld=True,
        schema={
            'image': f'{base_url}/static/favicon/logo_text.svg',
            'url': base_url + '/policy/',
            'logo': f'{base_url}/static/favicon/logo_text.svg',
            'name': 'Personal Data Processing Policy | KERATECH',
            'description': 'KERATECH Personal Data Processing Policy. '
                           'Information on the collection, use, '
                           'and protection of user data.',
            'email': 'keratekh@yandex.ru',
            'telephone': '+7-950-758-70-27',
            'address': {
                'streetAddress': 'Plekhanovskaya St., 66B, Office 411',
                'addressLocality': 'Voronezh',
                'postalCode': '394026',
                'addressCountry': 'Russia',
            }
        }
    )

    page = PolicyPage.load()

    context = {
        'meta': meta,
        'page': page,
    }

    return render(request, template_name, context)
