from django.urls import path
from . import views

urlpatterns = [
    path('', views.cake, name='cake'),
    path('<cake_order_number>/', views.cake_success, name='cake_order_success'),
]
