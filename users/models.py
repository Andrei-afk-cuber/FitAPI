from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


def check_email(value):
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
    weight = models.FloatField(default=0)
    activity_status = models.CharField(choices=ACTIVITY_CHOICES, max_length=5, default='*')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username