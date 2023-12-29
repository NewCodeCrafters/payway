import uuid
from django.db import models

from django.contrib.auth import get_user_model

from account.models import Account

User = get_user_model()


class Transactions(models.Model):
    ...


class Deposit(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trx_reference = models.CharField(
        max_length=15, blank=True, unique=True
    )  # auto generate this field
    self_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)


# str and save method


class InterWalletTransfer(models.Model):
    ...


class WalletTransfer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # trx_reference = models.CharField(max_length=15, blank=True, unique=True) # auto generate this field
    # self_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    # amount = models.DecimalField(max_digits=12, decimal_places=2)
    # created = models.DateTimeField(auto_now_add=True)
