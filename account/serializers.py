from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(decimal_places=2, max_digits=12, read_only=True)

    class Meta:
        model = Account
        fields = ("currency", "balance")
