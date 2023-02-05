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


ALLERGIES_CHOICES = (("gluten", "gluten"),
                     ("egg", "egg"),
                     ("nut", "nut"),
                     ("soy", "soy"),
                     ("milk", "milk"),
                     ("celery", "celery"),
                     ("mustard", "mustard"),
                     ("sesame_seed", "sesame seed"))


class Allergens(models.Model):
    allergy = models.CharField(max_length=11, choices=ALLERGIES_CHOICES)

    def __str__(self):
        return self.get_allergy_display()


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True,
        on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=False, blank=False)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    hidden = models.BooleanField(default=False)
    ingredients = models.TextField()
    allergens = models.ManyToManyField(Allergens)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.sku = self.name.replace(" ", "-").lower()
        super(Product, self).save(*args, **kwargs)
