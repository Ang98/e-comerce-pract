from django.db import models
from autoslug import AutoSlugField

from model_utils.models import TimeStampedModel
from products.models import Category

class Product(TimeStampedModel):
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    display = models.BooleanField(null=True, blank=True)
    display_in_home = models.BooleanField(null=True, blank=True)
    name = models.CharField(max_length = 150)
    offer_discount = models.PositiveSmallIntegerField(null=True, blank=True)
    order = models.PositiveSmallIntegerField(null=True, blank=True)
    price = models.DecimalField(decimal_places=3,max_digits=4)
    slug = AutoSlugField(populate_from='name')
    
    