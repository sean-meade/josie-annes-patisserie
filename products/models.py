import datetime

from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


ALLERGIES_CHOICES = (("gluten", "gluten"),
                     ("egg", "egg"),
                     ("nut", "nut"),
                     ("soy", "soy"),
                     ("milk", "milk"),
                     ("celery", "celery"),
                     ("mustard", "mustard"),
                     ("sesame_seed", "sesame seed"),
                     ("wheat", "wheat"),
                     ("sulphites", "sulphites"),
                     ("gelatine", "gelatine"))


class Allergens(models.Model):
    allergy = models.CharField(max_length=11, choices=ALLERGIES_CHOICES)

    def __str__(self):
        return self.get_allergy_display()

    def get_friendly_name(self):
        return self.allergy[0]


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = RichTextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    has_size = models.BooleanField(default=False)
    mince_pies = models.BooleanField(default=False)
    medium_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    large_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    hidden = models.BooleanField(default=False)
    ingredients = models.TextField(null=True, blank=True)
    allergens = models.ManyToManyField(Allergens, null=True, blank=True)
    individual_dessert = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.sku = self.name.replace(" ", "-").lower()
        super(Product, self).save(*args, **kwargs)
