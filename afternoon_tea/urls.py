from django.urls import path
from . import views

urlpatterns = [
    path('', views.afternoon_tea, name='afternoon_tea'),
    path('<booking_number>/', views.afternoon_tea_success, name='afternoon_tea_success'),
]
