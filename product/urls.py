from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:pk>/', views.detail, name='detail'),
]
