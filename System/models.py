from django.db import models
from django.utils.encoding import smart_unicode

class System(models.Model):
    name = models.CharField(max_length=120, null=False, blank=True)
    isActive = models.BooleanField()
 
    def __str__(self):
        return self.name