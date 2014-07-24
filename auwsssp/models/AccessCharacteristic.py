from django.db import models
from django.utils.encoding import smart_unicode

class AccessCharacteristic(models.Model):
    system = models.ForeignKey('System')
    name = models.CharField(max_length=120, null=False, blank=True)
    isActive = models.BooleanField()