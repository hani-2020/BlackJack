"""write your models here"""
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
import django.utils.timezone


class CustomUserManager(UserManager):
    """Since we switched out username for email a custom manager needs to be defined to handle making a superuser"""
    def create_superuser(self, email, password=None):
        user = self.model(email=email)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractUser):
    """User model which works with all auth"""
    birthday = models.DateField(default=django.utils.timezone.now)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='user/',null=True, blank=True)
    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.email)
        