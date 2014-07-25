from django.db import models
from django.utils.encoding import smart_unicode

class Country(models.Model):    
    name = models.CharField(max_length=120, null=False, blank=False)
    
    def __str__(self):
        return self.name

class PriorityArea(models.Model):
    country = models.ForeignKey('Country')
    name = models.CharField(max_length=100, null=False, blank=False)
    latitude = models.DecimalField(max_digits=19, decimal_places=10, null=False)
    longitude = models.DecimalField(max_digits=19, decimal_places=10, null=False)
    isActive = models.BooleanField()

class System(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    isActive = models.BooleanField()
 
    def __str__(self):
        return self.name
    
class AccessCharacteristic(models.Model):
    system = models.ForeignKey('System')
    name = models.CharField(max_length=120, null=False, blank=False)
    isActive = models.BooleanField()
    
class AccessProperty(models.Model):
    accessCharacteristic = models.ForeignKey('AccessCharacteristic')
    name = models.CharField(max_length=120, null=False, blank=False)
    isActive = models.BooleanField()
    
    class Meta:
        verbose_name_plural = "Access Properties"
     
class SectorPerformanceCategory(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    isActive = models.BooleanField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Performance Categories"
        
    

class TenderProcedureProperty(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    isActive = models.BooleanField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Tender Procedure Properties"
    
