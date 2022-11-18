from django.contrib import admin
from .models import Product, Category, Allergens
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):

    list_display = ("name", "friendly_name")


@admin.register(Allergens)
class AllergensAdmin(SummernoteModelAdmin):

    list_display = ("allergy", )


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):

    prepopulated_fields = {"sku": ("name",)}
    list_display = ("sku", "name", "price", "hidden")
    search_fields = ["name", "body"]

    ordering = ("sku",)
