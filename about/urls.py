from django.urls import path

from about import views

app_name = 'about'

urlpatterns = [
    path('', views.index, name='index'),
]
