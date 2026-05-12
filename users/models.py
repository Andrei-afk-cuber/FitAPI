from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
)
from django.db import models


# email validator
def check_email(value: str) -> None:
    if "@" not in value:
        raise ValidationError("Email must contain a '@'")


# Create your models here.
class User(AbstractUser):
    # values for choices fields
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]

    ACTIVITY_CHOICES = [
        (1, "Not active"),
        (2, "Light"),
        (3, "Medium"),
        (4, "High"),
        (5, "Very high"),
    ]

    TARGET_CHOICES = [
        ("loss", "Weight loss"),
        ("maintain", "Maintenance"),
        ("gain", "Gaining muscle mass"),
    ]

    # fields
    username = models.CharField(null=True, blank=True, max_length=50)
    email = models.EmailField(max_length=50, validators=[check_email])
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")
    weight = models.FloatField(blank=False)
    height = models.FloatField(blank=False)
    age = models.IntegerField(
        validators=[MinValueValidator(16), MaxValueValidator(100)]
    )
    activity_status = models.CharField(
        choices=ACTIVITY_CHOICES, max_length=5, default="*"
    )
    target = models.CharField(
        choices=TARGET_CHOICES, max_length=20, default="weight maintenance"
    )
    body_mass_index = models.FloatField(default=0)
    password = models.CharField(blank=False, validators=[MinLengthValidator(8)])

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return f"{self.id}. {self.first_name} {self.last_name}"
