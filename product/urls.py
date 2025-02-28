from django.urls import path

from .views import product_detail, product_list, type_detail

app_name = 'product'

urlpatterns = [
    path('type/<slug:slug>/', type_detail, name='type_detail'),
    path('', product_list, name='product_list'),
    path('<slug:slug>/', product_detail, name='product_detail'),
]
