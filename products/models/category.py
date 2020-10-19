from django.db import models
from autoslug import AutoSlugField

class Category(models.Model):
    
    created = models.DateField(auto_now_add=True)
    display = models.BooleanField()
    display_in_home = models.BooleanField()
    modified = models.DateField(auto_now=True)
    name = models.CharField(max_length = 150)
    order = models.PositiveSmallIntegerField()
    slug = AutoSlugField(populate_from='name')
    