from django.urls import path

from article import views

app_name = 'article'

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:pk>/', views.detail, name='detail'),
]
