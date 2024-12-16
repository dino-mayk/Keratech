from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [
    path('type/<slug:slug>/', views.type_detail, name='type_detail'),
    path('', views.product_list, name='product_list'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
