from rest_framework import serializers

from .models import Account, CurrrencyChoice, TransactionChoices, Transactions, User


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ("account_number", "transaction_type", "amount")


class InterTransferSerializer(serializers.Serializer):
    account_number = serializers.IntegerField()
    transaction_type = serializers.CharField(default="TRANSFER")
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
