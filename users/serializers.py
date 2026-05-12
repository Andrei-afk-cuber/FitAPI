from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User


# serializer for get users list
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "gender", "age")


# serializer for get user profile
class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "gender",
            "age",
            "weight",
            "height",
            "activity_status",
            "is_active",
            "body_mass_index"
        )


# serializer for create user
class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    repeat_password = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    body_mass_index = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "gender",
            "weight",
            "height",
            "age",
            "body_mass_index",
            "activity_status",
            "target",
            "email",
            "password",
            "repeat_password",
        )

    # calculate body mass index
    def get_body_mass_index(self, obj):
        return round(obj.weight / (obj.height / 100) ** 2, 1)

    # check email unique
    def validate_email(self, value):
        if User.objects.filter(email=value, is_active=True).exists():
            raise ValidationError("Active user with this email already exists")

        return value

    # validate password and repeat_password
    def validate(self, attrs):
        if attrs["password"] == attrs["repeat_password"]:
            attrs.pop("repeat_password")
            return attrs
        raise ValidationError("Password does not match")

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


# serializer for update user
class UserUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "weight", "height", "age")
