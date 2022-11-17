from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    hidden = models.BooleanField(default=False)
    ingredients = models.TextField()
    gluten = models.BooleanField(default=False)
    egg = models.BooleanField(default=False)
    nut = models.BooleanField(default=False)
    soy = models.BooleanField(default=False)
    milk = models.BooleanField(default=False)
    celery = models.BooleanField(default=False)
    mustard = models.BooleanField(default=False)
    sesame_seed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
