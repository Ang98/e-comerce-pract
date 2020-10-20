from django.db import models

from model_utils.models import TimeStampedModel

from products.models import Color,Product

class Stock(TimeStampedModel):
    
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    
    
    
    