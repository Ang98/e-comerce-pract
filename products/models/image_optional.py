from django.db import models

from model_utils.models import TimeStampedModel

from products.models import Product

class ImageOptional(TimeStampedModel):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    
    
    