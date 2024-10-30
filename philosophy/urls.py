from django.urls import path

from philosophy import views

app_name = 'philosophy'

urlpatterns = [
    path('', views.index, name='index'),
]
