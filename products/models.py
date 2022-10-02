from django.db import models
from cloudinary.models import CloudinaryField


class Product(models.Model):

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = CloudinaryField("image", default="placeholder")
    delivery = models.BooleanField(default=False)
    collection = models.BooleanField(default=False)
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
    fish = models.BooleanField(default=False)

    def __str__(self):
        return self.name
