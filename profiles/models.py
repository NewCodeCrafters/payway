from django.db import models

from django.contrib.auth import get_user_model
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
)
from django_countries.fields import CountryField


User = get_user_model()


class CurrrencyChoice(models.TextChoices):
    USD = "USD"
    CAD = "CAD"
    NGN = "NGN"
    GBP = "GBP"
    EUR = "EUR"
    AUD = "AUD"
    GHC = "GHC"


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(
        max_length=11, validators=[MinLengthValidator(10)], blank=True
    )
    address = models.CharField(max_length=100, blank=True)
    country = CountryField(blank=True)
    dob = models.DateField(null=True)
    currency = models.CharField(
        max_length=100, choices=CurrrencyChoice.choices, blank=True
    )


# str

# save

# signals
# Create a new app called accounts
#
