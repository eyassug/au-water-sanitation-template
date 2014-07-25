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
    is_active = models.BooleanField()
    
    def __str__(self):
        return self.name + ' - ' + self.country.name

    class Meta:
        verbose_name_plural = "Priority Areas"
     
class SectorCategory(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    is_active = models.BooleanField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Sector Categories"
        
    

class TenderProcedureProperty(models.Model):
    sector_category = models.ForeignKey('SectorCategory')
    name = models.CharField(max_length=120, null=False, blank=False)
    is_active = models.BooleanField()
    
    def __str__(self):
        return self.name + ' - ' + self.sector_category.name
    
    class Meta:
        verbose_name_plural = "Tender & Procedure Properties"
    
class Technology(models.Model):
    facility_character = models.ForeignKey('FacilityCharacter')
    name = models.CharField(max_length=120, null=False, blank=False)
    is_active = models.BooleanField()
   
    def __str__(self):
        return self.name + ' - ' + self.sector_category.name
    
    class Meta:
        verbose_name_plural = "Technologies"
        
class FacilityCharacter(models.Model):
    sector_category = models.ForeignKey('SectorCategory')
    name = models.CharField(max_length=120, null=False, blank=False)
    is_active = models.BooleanField()
   
    def __str__(self):
        return self.name + ' - ' + self.sector_category.name
        
    class Meta:
        verbose_name_plural = "Facility Characters"
        
class CountryDemographic(models.Model):
    country = models.ForeignKey('Country')
    year = models.IntegerField(null=False,blank=False)
    population = models.IntegerField(null=False,blank=False)