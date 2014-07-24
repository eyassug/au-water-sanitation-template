from django.db import models
from django.utils.encoding import smart_unicode

class AccessProperty(models.Model):
    accessCharacteristic = models.ForeignKey('AccessCharacteristic')
    name = models.CharField(max_length=120, null=False, blank=True)
    isActive = models.BooleanField()
    