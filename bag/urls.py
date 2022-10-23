from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='bag'),
    path('add/<item_id>', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>', views.remove_bag_item, name='remove_bag_item'),
]
