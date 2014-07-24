from django.db import models
from django.utils.encoding import smart_unicode

class SectorPerformanceCategory(models.Model):
    name = models.CharField(max_length=120, null=False, blank=True)
    isActive = models.BooleanField()