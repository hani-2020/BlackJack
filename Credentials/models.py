"""models are written here"""
from django.db import models

class User(models.Model):
    """
    user table will have these fields
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    current_balance = models.IntegerField()
    birthday = models.DateField()

    def __str__(self):
        return str(self.first_name)
    