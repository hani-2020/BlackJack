"""write your models here"""
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """User model which works with all auth"""
    birthday = models.DateField()
    current_balance = models.IntegerField(default=1000)
    email = models.EmailField(unique=True)
    username = None

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.email)
    