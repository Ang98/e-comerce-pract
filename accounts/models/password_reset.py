from django.db import models
from django.contrib.auth.models import User


class PasswordReset(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    expiration_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    last_updated = models.DateTimeField(auto_now=False, auto_now_add=False)    
    reset_code = models.IntegerField()
    used = models.BooleanField()