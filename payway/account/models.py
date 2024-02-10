from django.db import models
from django.contrib.auth import get_user_model
from account.utils import (
    generate_account_number,
    generate_aud_account_number,
    generate_canada_account_number,
    generate_euros_account_number,
    generate_ghc_account_number,
    generate_naira_account_number,
    generate_pounds_account_number,
)

from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
)

User = get_user_model()


class CurrrencyChoice(models.TextChoices):
    USD = "USD"
    CAD = "CAD"
    NGN = "NGN"
    GBP = "GBP"
    EUR = "EUR"
    AUD = "AUD"
    GHC = "GHC"


class Account(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="account_user"
    )
    account_number = models.CharField(
        max_length=11, validators=[MinLengthValidator(10)], blank=True
    )
    currency = models.CharField(max_length=10, choices=CurrrencyChoice.choices)
    balance = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    is_approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.currency} account"

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
        unique_together = ("user", "currency")

    def save(self, *args, **kwargs):
        if not self.account_number and self.currency == "USD":
            self.account_number = generate_naira_account_number(self.currency)
        elif not self.account_number and self.currency == "NGN":
            self.account_number = generate_naira_account_number(self.currency)
        elif not self.account_number and self.currency == "CAD":
            self.account_number = generate_canada_account_number(self.currency)
        elif not self.account_number and self.currency == "GBP":
            self.account_number = generate_pounds_account_number(self.currency)
        elif not self.account_number and self.currency == "EUR":
            self.account_number = generate_euros_account_number(self.currency)
        elif not self.account_number and self.currency == "AUD":
            self.account_number = generate_aud_account_number(self.currency)
        elif not self.account_number and self.currency == "GHC":
            self.account_number = generate_ghc_account_number(self.currency)
        else:
            self.account_number = self.account_number
        super().save(*args, **kwargs)
