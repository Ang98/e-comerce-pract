from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=9)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    
    