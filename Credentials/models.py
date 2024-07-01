"""write your models here"""
from django.db import models
from django.contrib.auth.models import AbstractUser
import django.utils.timezone

class User(AbstractUser):
    """User model which works with all auth"""
    birthday = models.DateField(default=django.utils.timezone.now)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)
    email = models.EmailField(unique=True)
    username = None

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.email)
    