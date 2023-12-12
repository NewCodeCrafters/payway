from rest_framework import serializers
from .models import Profiles
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        email = serializers.CharField(
            read_only=True,
            max_length=100,
        )
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

    class Meta:
        model = Profiles
        fields = ("user", "address", "country", "dob", "currency", "account_number")


# class UpdateSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
