from django.db import models

from django.contrib.auth import get_user_model
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
)
from django_countries.fields import CountryField
from .utils import generate_unique_account_number


User = get_user_model()


class CurrrencyChoice(models.TextChoices):
    USD = "USD"
    CAD = "CAD"
    NGN = "NGN"
    GBP = "GBP"
    EUR = "EUR"
    AUD = "AUD"
    GHC = "GHC"


class CardType(models.TextChoices):
    Passport = "Passport"
    NIN = "NIN"
    BVN = "BVN"
    Drivers_license = "Drivers_license"


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # account_number = models.CharField(
    #     max_length=11, validators=[MinLengthValidator(10)], blank=True
    # )
    address = models.CharField(max_length=100, blank=True)
    country = CountryField(blank=True)
    dob = models.DateField(null=True, blank=True)
    profile_pics = models.ImageField(upload_to="hahhaha", blank=True)
    currency = models.CharField(
        max_length=100, choices=CurrrencyChoice.choices, blank=True
    )
    document_type = models.CharField(
        max_length=100, choices=CardType.choices, blank=True
    )
    document = models.ImageField(upload_to="documents", blank=True)
    doc_verified = models.BooleanField(default=False)
    balance = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    document = models.FileField(upload_to="hahhaha", null=True, blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user.last_name}'s profile"

    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = generate_unique_account_number()
        if self.country == "NG":
            self.currency = CurrrencyChoice.NGN.upper()
        elif self.country == "CA":
            self.currency = CurrrencyChoice.CAD.upper()
        elif self.country == "US":
            self.currency = CurrrencyChoice.USD.upper()
        elif self.country == "UK":
            self.currency = CurrrencyChoice.GBP.upper()
        elif self.country == "AU":
            self.currency = CurrrencyChoice.AUD.upper()
        elif self.country == "IT" or self.country == "PL" or self.country == "DE":
            self.currency = CurrrencyChoice.EUR.upper()
        elif self.country == "GH":
            self.currency = CurrrencyChoice.GHC.upper()
        else:
            self.currency = CurrrencyChoice.USD.upper()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
