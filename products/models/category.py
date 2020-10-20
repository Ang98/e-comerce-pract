from django.db import models
from autoslug import AutoSlugField
from stdimage import StdImageField

from model_utils.models import TimeStampedModel

class Category(TimeStampedModel):
    
    display = models.BooleanField()
    display_in_home = models.BooleanField()
    #image = StdImageField()
    name = models.CharField(max_length = 150)
    order = models.PositiveSmallIntegerField()
    slug = AutoSlugField(populate_from='name')
    