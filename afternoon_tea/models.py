import uuid

from django.db import models
from profiles.models import UserProfile
import datetime


three_weeks_from_now = datetime.date.today() + datetime.timedelta(days=21)

next_saturday = datetime.timedelta((12 - three_weeks_from_now.weekday()) % 7) + three_weeks_from_now

DATE_CHOICES = []

current_day = next_saturday

for i in range(1, 4):

    DATE_CHOICES.append((current_day, current_day.strftime('%a: %b %d')))
    current_day = current_day + datetime.timedelta(days=1)
    DATE_CHOICES.append((current_day, current_day.strftime('%a: %b %d')))
    current_day = current_day + datetime.timedelta(days=6)

TIME_CHOICES = (
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
    )


class AfternoonTea(models.Model):
    booking_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateField(auto_now_add=False, choices=DATE_CHOICES)
    time = models.CharField(max_length=6, choices=TIME_CHOICES, default='green')
    notes = models.TextField()
    under_review = models.BooleanField(default=True)
    no_of_people = models.PositiveIntegerField(null=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_no_of_people_range",
                check=models.Q(no_of_people__range=(1, 25_000)),
            ),
        ]

    def _generate_booking_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.booking_number:
            self.booking_number = self._generate_booking_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.booking_number
