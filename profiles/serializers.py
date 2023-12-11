from rest_framework import serializers

from .models import Profiles


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ("address", "address", "country")
