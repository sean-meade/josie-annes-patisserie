from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<str:sku>/', views.find_product, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<str:sku>/', views.edit_product, name='edit_product'),
    path('delete/<str:sku>/', views.delete_product, name='delete_product'),
]
