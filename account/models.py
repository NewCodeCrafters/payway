from django.db import models
from django.contrib.auth import get_user_model
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=11, validators=[MinLengthValidator(10)], blank=True)
    currency = models.CharField(max_length=10, choices=CurrrencyChoice.choices, blank=True)
    balance = models.FloatField()
    is_active = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user}'s account"
    
    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"



