import uuid

from django.db import models
from profiles.models import UserProfile
import datetime


three_weeks_from_now = datetime.date.today() + datetime.timedelta(days=21)

DATE_CHOICES = []


class Cake(models.Model):

    cake_order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateField(auto_now_add=False)
    notes = models.TextField()
    under_review = models.BooleanField(default=True)


    def _generate_cake_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.cake_order_number:
            self.cake_order_number = self._generate_cake_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.cake_order_number
