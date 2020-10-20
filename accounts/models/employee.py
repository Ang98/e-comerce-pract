from django.db import models
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel

class Employee(TimeStampedModel):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)