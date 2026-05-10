from rest_framework import serializers

from .models import User


# TODO: доделать сериализатор
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'gender', 'weight', 'email', 'password', 'repeat_password')