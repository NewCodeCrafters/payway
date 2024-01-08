from rest_framework import serializers
from .models import Profiles
from user.models import User
from djoser.serializers import UserCreateSerializer, UserSerializer


class UserSerializer(UserSerializer):
    email = serializers.EmailField(
        read_only=True,
        max_length=100,
    )

    class Meta:
        model = User
        ref_name = "UserSerializer"
        fields = ("email", "first_name", "last_name", "phone_number")


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    currency = serializers.CharField(
        read_only=True,
        max_length=100,
    )
    account_number = serializers.CharField(max_length=100, read_only=True)
    country = serializers.CharField(max_length=100)
    dob = serializers.DateField(read_only=True)
    balance = serializers.DecimalField(read_only=True, max_digits=100, decimal_places=2)

    class Meta:
        model = Profiles
        ref_name = "ProfileSerializer"
        fields = (
            "user",
            "address",
            "country",
            "dob",
            "currency",
            "account_number",
            "balance",
        )


# class UpdateSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
