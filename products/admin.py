from django.contrib import admin
from .models import Product
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):

    prepopulated_fields = {"sku": ("name",)}
    list_display = ("name", "price", "hidden")
    search_fields = ["name", "body"]
