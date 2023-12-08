from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from django.core.validators import EmailValidator

from .models import User


class CustomUserSerializer(UserSerializer):
    email = serializers.EmailField(
        validators=[EmailValidator()],
        required=True,
    )

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "phone_number",
            "first_name",
            "last_name",
        )
