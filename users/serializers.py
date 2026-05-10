from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    repeat_password = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'gender', 'weight', 'height', 'age', 'email', 'password', 'repeat_password')

    # validate password and repeat_password
    def validate(self, attrs):
        if attrs['password'] == attrs['repeat_password']:
            attrs.pop('repeat_password')
            return attrs
        raise ValidationError('Password does not match')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

# serializer for update user
class UserUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'weight', 'height', 'age')