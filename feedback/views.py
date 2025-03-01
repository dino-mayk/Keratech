from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .models import Feedback


def feedback_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not name or not email or not message:
            messages.error(request, 'Пожалуйста, заполните все поля.')
        elif '@' not in email:
            messages.error(request, 'Пожалуйста, введите корректный email.')
        else:
            Feedback.objects.create(name=name, email=email, message=message)

            superuser_emails = list(
                User.objects.filter(
                    is_superuser=True,
                    email__isnull=False,
                ).values_list('email', flat=True)
            )

            if superuser_emails == ['']:
                messages.warning(
                    request,
                    'Нет активных администраторов для уведомления.',
                )
            else:
                subject = 'Новое сообщение обратной связи'
                body = f'Отправитель: {name}\n' + \
                    f'Email: {email}\nСообщение:\n{message}'
                from_email = settings.DEFAULT_FROM_EMAIL

                try:
                    send_mail(
                        subject, body,
                        from_email,
                        superuser_emails,
                        fail_silently=False,
                    )
                    messages.success(
                        request,
                        'Ваше сообщение успешно отправлено! '
                        'Администраторы уведомлены.',
                    )
                except Exception as e:
                    print(e)
                    messages.warning(
                        request,
                        'Ваше сообщение успешно отправлено, '
                        'но произошла ошибка при уведомлении администраторов.',
                    )

            return redirect(reverse_lazy('homepage:index'))

    return render(request, 'homepage/index.html')
