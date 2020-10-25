from django.db import models

from model_utils.models import TimeStampedModel

class Color(TimeStampedModel):
    
    hex_code = models.CharField(max_length = 150)    
    name = models.CharField(max_length = 150)