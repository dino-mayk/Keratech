from django.contrib import messages
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
            messages.success(request, 'Ваше сообщение успешно отправлено!')
            return redirect(reverse_lazy('homepage:index'))

    return render(request, 'homepage/index.html')
