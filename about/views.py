from django.shortcuts import render
from meta.views import Meta


def index(request):
    template_name = 'about/index.html'

    protocol = request.scheme
    host = request.get_host()
    base_url = f'{protocol}://{host}'

    meta = Meta(
        title='Контакты КЕРАТЕХ - огнеупорные и изоляционные материалы',
        description='Контактная информация компании КЕРАТЕХ. '
                    'Телефон: +7 (950) 758-70-27, '
                    'адрес: г. Воронеж, ул. Плехановская, д. 66Б, оф. 411. '
                    'Электронная почта: keratekh@yandex.ru. '
                    'Найдите нас на карте.',
        keywords=[
            'КЕРАТЕХ', 'контакты', 'огнеупорные материалы',
            'изоляционные материалы', 'Воронеж', 'адрес производства',
            'контактный телефон', 'электронная почта',
        ],
        url=request.build_absolute_uri(),
        object_type='Organization',
        site_name='Keratech',
        schemaorg_type='Organization',
        schemaorg_title='Keratech Contacts',
        use_json_ld=True,
        schema={
            'image': f'{base_url}/static/favicon/logo_text.svg',
            'url': base_url + '/contacts/',
            'logo': f'{base_url}/static/favicon/logo_text.svg',
            'name': 'Contacts of KERATECH - Refractory and Insulating '
                    'Materials',
            'description': 'Contact information for KERATECH. '
                    'Phone: +7 (950) 758-70-27, '
                    'Address: Voronezh, Plekhanovskaya St., 66B, '
                    'Office 411. '
                    'Email: keratekh@yandex.ru.',
            'email': 'keratekh@yandex.ru',
            'telephone': '+7-950-758-70-27',
            'address': {
                'streetAddress': 'Plekhanovskaya St., 66B, Office 411',
                'addressLocality': 'Voronezh',
                'postalCode': '394026',
                'addressCountry': 'Russia'
            }
        }
    )
    context = {
        'meta': meta,
    }
    return render(request, template_name, context)
