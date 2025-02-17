from django.urls import path

from core import views

urlpatterns = [
    path('robots.txt', views.robots_txt, name='robots_txt'),
]
