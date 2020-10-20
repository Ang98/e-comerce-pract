from django.db import models
from autoslug import AutoSlugField

from model_utils.models import TimeStampedModel

class Product(TimeStampedModel):
    
    description = models.TextField()
    display = models.BooleanField()
    display_in_home = models.BooleanField()
    name = models.CharField(max_length = 150)
    offer_discount = models.PositiveSmallIntegerField()
    order = models.PositiveSmallIntegerField()
    price = models.DecimalField(decimal_places=2,max_digits=4)
    slug = AutoSlugField(populate_from='name')
    
    