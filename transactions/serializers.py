from rest_framework import serializers

from .models import Account, CurrrencyChoice, TransactionChoices, Transactions, User


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ("account_number", "transaction_type", "amount")
