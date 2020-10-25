from django.db import models

from model_utils.models import TimeStampedModel
from stdimage import StdImageField


from products.models import Product

class ImageOptional(TimeStampedModel):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = StdImageField()
    
    
    