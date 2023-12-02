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

    def __str__(self) -> str:
        return f"{self.user}'s profile"
    # def save(self, *args, **kwargs):
    #     if self.country == "Nigeria":
    #         self.currency = "NGN"
    #     elif self.country == "Canada":
    #         self.currency = "CAD"
    #     elif self.country == "United States":
    #         self.currency = "USD",
    #     elif self.country == "United Kingdom":
    #         self.currency = "GBP",
    #     elif self.country== "Australia":
    #         self.currency = "AUD",
    #     elif self.country == "Europe":
    #         self.currency = "EUR",
    #     elif self.country == "Ghana":
    #         self.currency = "GHC",
    #     else C        
    #     return super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        country_currency_mapping = {
            'US': CurrrencyChoice.USD,
            'CA': CurrrencyChoice.CAD,
            'NG': CurrrencyChoice.NGN,
            'GB': CurrrencyChoice.GBP,
            'DE': CurrrencyChoice.EUR,
            'AU': CurrrencyChoice.AUD,
        }
        if self.country:
                country_code = self.country.code
                if country_code in country_currency_mapping:
                    self.currency = country_currency_mapping[country_code]
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"



# str

# save

# signals
# Create a new app called accounts
#
