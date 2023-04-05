from rest_framework import serializers

from .models import User


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['reference_id', 'profile_picture', 'username', 'first_name', 'last_name']
