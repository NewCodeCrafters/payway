from rest_framework import serializers

from .models import Account, CurrrencyChoice, TransactionChoices, Transactions, User


class DepositSerializer(serializers.ModelSerializer):
    account_number = serializers.CharField(max_length=20, read_only=True)
    balance = serializers.DecimalField(decimal_places=2, max_digits=12, read_only=True)
    currency = serializers.ChoiceField(choices=CurrrencyChoice.choices, read_only=True)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Account
        fields = ("currency", "balance", "account_number")


class TransferSerializer(serializers.Serializer):
    currency = serializers.ChoiceField(choices=CurrrencyChoice.choices)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    from_acc = serializers.CharField(max_length=13, choices=CurrrencyChoice.choices)
    account_number = serializers.CharField(max_length=20)
    transaction_type = serializers.CharField(
        max_length=30, choices=TransactionChoices.choices
    )
