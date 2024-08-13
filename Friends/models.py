from django.db import models
from Credentials.models import User

class Friends(models.Model):
    friend1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friend1_to_user")
    friend2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friend2_to_user")
    accepted = models.BooleanField(default=False)
