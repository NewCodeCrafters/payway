from django.utils import timezone
import uuid
from django.db import models
from django.contrib.auth import get_user_model
from account.models import Account, CurrrencyChoice
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
)
from transactions.utils import generate_transaction_reference, generate_trf_id

User = get_user_model()


class StatusChoice(models.TextChoices):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    FAILED = "FAILED"


class Deposit(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trx_reference = models.CharField(max_length=15, blank=True, unique=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=StatusChoice.choices)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.id}"

    class Meta:
        verbose_name = "Deposit"
        verbose_name_plural = "Deposits"


class TransactionChoices(models.TextChoices):
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"
    TRANSFER = "TRANSFER"


class Transactions(models.Model):
    trf_id = models.CharField(max_length=10, verbose_name="Transaction Reference ID")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transaction_user"
    )
    account_number = models.CharField(max_length=13)
    transaction_type = models.CharField(
        max_length=30, choices=TransactionChoices.choices
    )
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=StatusChoice.choices)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.transaction_type} of {self.amount} to {self.currency}"

    def save(self, *args, **kwargs):
        if not self.trf_id:
            self.trf_id = generate_trf_id()
        super().save(*args, **kwargs)
