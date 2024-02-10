from rest_framework import serializers

from .models import Account, CurrrencyChoice


class AccountSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(decimal_places=2, max_digits=12, read_only=True)
    account_number = serializers.CharField(max_length=20, read_only=True)

    class Meta:
        model = Account
        fields = ("currency", "balance", "account_number")


class AdminAccountSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(decimal_places=2, max_digits=12, read_only=True)
    account_number = serializers.CharField(max_length=20, read_only=True)

    class Meta:
        model = Account
        fields = (
            "currency",
            "balance",
            "account_number",
        )


class WalletTransferSerializer(serializers.Serializer):
    currency = serializers.ChoiceField(choices=CurrrencyChoice.choices)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
