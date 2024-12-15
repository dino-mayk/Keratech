from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [
    path('type/<int:pk>/', views.type_detail, name='type_detail'),
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
]
