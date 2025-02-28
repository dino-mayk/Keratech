from django.urls import path

from .views import feedback_create

app_name = 'feedback'

urlpatterns = [
    path('create/', feedback_create, name='create'),
]
