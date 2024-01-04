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
from transactions.utils import generate_transaction_reference

User = get_user_model()


class Transactions(models.Model):
    ...


class Deposit(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trx_reference = models.CharField(max_length=15, blank=True, unique=True)
    self_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.id}"

    class Meta:
        verbose_name = "Deposit"
        verbose_name_plural = "Deposits"


class ExchangeRate(models.Model):
    source_currency = models.CharField(max_length=10, choices=CurrrencyChoice.choices)
    target_currency = models.CharField(max_length=10, choices=CurrrencyChoice.choices)
    rate = models.DecimalField(decimal_places=4, max_digits=10)

    def __str__(self) -> str:
        return f"{self.source_currency} to {self.target_currency} - Rate: {self.rate}"


class InterwalletSwap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source_account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="source_account"
    )
    target_account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="target_account"
    )
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    exchange_rate = models.DecimalField(
        decimal_places=4, max_digits=10, null=True, blank=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Interwallet Swap - {self.user.username} - {self.timestamp}"

    def calculate_exchange_rate(self):
        source_currency = self.source_account.currency
        target_currency = self.target_account.currency
        try:
            exchange_rate_obj = ExchangeRate.objects.get(
                source_currency=source_currency, target_currency=target_currency
            )
            return exchange_rate_obj.rate
        except ExchangeRate.DoesNotExist:
            return None

    def save(self, *args, **kwargs):
        self.exchange_rate = self.calculate_exchange_rate()
        if self.exchange_rate is not None:
            target_amount = self.amount * self.exchange_rate
            self.target_account.balance += target_amount
            self.source_account.balance -= self.amount
            self.target_account.save()
            self.source_account.save()

        super().save(*args, **kwargs)


class WalletTransfer(models.Model):
    sender_account = models.ForeignKey(Account, on_delete=models.CASCADE, default=None)
    receiver_account_number = models.CharField(
        max_length=11, validators=[MinLengthValidator(10)], default=None
    )
    amount = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    transaction_reference = models.CharField(max_length=10, unique=True, default="")
    time_sent = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Transfer from {self.sender_account.currency} account to {self.receiver_account_number}"

    def save(self, *args, **kwargs):
        self.sender_account.balance -= self.amount
        self.sender_account.save()
        if not self.transaction_reference:
            self.transaction_reference = generate_transaction_reference()

        if not self.sender_account:
            default_sender_account_id = 1
            self.sender_account = Account.objects.get(pk=default_sender_account_id)
