from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


# email validator
def check_email(value: str) -> None:
    if '@' not in value:
        raise ValidationError('Email must contain a \'@\'')

# password validator
def check_password(value: str) -> None:
    if len(value) < 8:
        raise ValidationError('Password must be at least 8 characters long')

    if value == value.lower() or value == value.upper():
        raise ValidationError('Password must contain upper and lower case letters')

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
    weight = models.FloatField(default=0)
    activity_status = models.CharField(choices=ACTIVITY_CHOICES, max_length=5, default='*')
    password = models.CharField(max_length=50, blank=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self) -> str:
        return f'{self.id}. {self.first_name} {self.last_name}'