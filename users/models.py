from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models


# email validator
def check_email(value: str) -> None:
    if '@' not in value:
        raise ValidationError('Email must contain a \'@\'')

# Create your models here.
class User(AbstractUser):
    # values for choices fields
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    ACTIVITY_CHOICES = [
        ('*', 'Not active'),
        ('**', 'Medium'),
        ('***', 'Active'),
        ('****', 'Very active')
    ]

    # fields
    email = models.EmailField(max_length=50, unique=True, validators=[check_email])
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    weight = models.FloatField(blank=False)
    height = models.FloatField(blank=False)
    age = models.IntegerField(validators=[MinValueValidator(16), MaxValueValidator(100)])
    activity_status = models.CharField(choices=ACTIVITY_CHOICES, max_length=5, default='*')
    password = models.CharField(blank=False, validators=[MinLengthValidator(8)])
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'weight', 'height', 'age', 'activity_status']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self) -> str:
        return f'{self.id}. {self.first_name} {self.last_name}'