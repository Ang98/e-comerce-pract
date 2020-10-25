from django.db import models
from autoslug import AutoSlugField
from stdimage import StdImageField

from model_utils.models import TimeStampedModel

class Category(TimeStampedModel):
    
    display = models.BooleanField(null=True, blank=True)
    display_in_home = models.BooleanField(null=True, blank=True)
    #image = StdImageField()
    name = models.CharField(max_length = 150)
    order = models.PositiveSmallIntegerField(null=True, blank=True)
    slug = AutoSlugField(populate_from='name')
    