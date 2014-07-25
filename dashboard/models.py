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

#class System(models.Model):
    #name = models.CharField(max_length=120, null=False, blank=False)
    #is_active = models.BooleanField()
 
    #def __str__(self):
       # return self.name
    
#class AccessCharacteristic(models.Model):
   # system = models.ForeignKey('System')
    #name = models.CharField(max_length=120, null=False, blank=False)
    #is_active = models.BooleanField()
    
#class AccessProperty(models.Model):
   # accessCharacteristic = models.ForeignKey('AccessCharacteristic')
   #name = models.CharField(max_length=120, null=False, blank=False)
    #is_active = models.BooleanField()
    
   # class Meta:
      #  verbose_name_plural = "Access Properties"
     
class SectorCategory(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    is_active = models.BooleanField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Sector Categories"
        
    

class TenderProcedureProperty(models.Model):
    sector_category = models.ForeignKey('SectorCategory')
    tender_proc_property = models.CharField(max_length=120, null=False, blank=False)
    is_active = models.BooleanField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Tender & Procedure Properties"
    
class Technology(models.Model):
    sector_category = models.ForeignKey('SectorCategory')
    facility_character = models.ForeignKey('FacilityCharacter')
    new_technology = models.CharField(max_length=120, null=False, blank=False)
    
    def __str__(self):
        return self.new_technology;
    class Meta:
        verbose_name_plural = "Technology"
        
class FacilityCharacter(models.Model):
    sector_category = models.ForeignKey('SectorCategory')
    facility_character = models.CharField(max_length=120, null=False, blank=False)
    
    def __str__(self):
        return self.facility_character
    class Meta:
        verbose_name_plural = "Facility Character"
        
    