from django.db import models
from django.contrib.auth.models import User


class PasswordReset(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_code = models.IntegerField()
    used = models.BooleanField()