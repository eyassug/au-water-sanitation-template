from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User

class Country(models.Model):    
    name = models.CharField(max_length=120, null=False, blank=False)
    
    def __str__(self):
        return self.name 
    class Meta:
        ordering = ['name']
    
class UserCountry(models.Model):
    user = models.OneToOneField(User)
    country = models.ForeignKey('country')
    
    def __str__(self):
        return self.country.name 
    class Meta:
        ordering = ['country']
    

class Period(models.Model):    
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    
    def __str__(self):
        return str(self.start_year) + '-' + str(self.end_year)
    
    class Meta:
        ordering = ['start_year']
    
class PriorityArea(models.Model):
    country = models.ForeignKey('Country')
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    latitude = models.DecimalField(max_digits=19, decimal_places=10, null=False, blank=True)
    longitude = models.DecimalField(max_digits=19, decimal_places=10, null=False, blank=True)
    is_active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Priority Areas"
        unique_together = ("country", "name")
        ordering = ['name']
class SectorCategory(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Sector Categories"
        ordering = ['name']
        
    

class TenderProcedureProperty(models.Model):
    sector_category = models.ForeignKey('SectorCategory')
    name = models.CharField(max_length=120, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name + ' - ' + self.sector_category.name
    
    
    class Meta:
        verbose_name_plural = "Tender & Procedure Properties"
        ordering = ['name']
        unique_together = ("sector_category", "name")
    
class Technology(models.Model):
    facility_character = models.ForeignKey('FacilityCharacter')
    name = models.CharField(max_length=120, null=False, blank=False, unique=False, verbose_name = "Technology")
    is_active = models.BooleanField(default=True)
   
    def __str__(self):
        return self.name #+ ' - ' + self.facility_character.name + ' - ' + self.facility_character.sector_category.name
    
    class Meta:
        verbose_name_plural = "Technologies"
        ordering = ['name']
        unique_together = ("facility_character", "name")
        
class FacilityCharacter(models.Model):
    sector_category = models.ForeignKey('SectorCategory')
    name = models.CharField(max_length=120, null=False, blank=False, unique=True)
    is_active = models.BooleanField(default=True)
   
    def __str__(self):
        return self.name 
    
        
    class Meta:
        verbose_name_plural = "Facility Characters"
        ordering = ['name']
        unique_together = ("sector_category", "name")
    
class CommunityApproachType(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Community Approach Types"
        ordering = ['name']
    
class Partner(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False, unique=True)
    mission = models.TextField()
    key_activities = models.TextField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Partners"
        ordering = ['name']

class Event(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False, unique=True)
    date = models.DateField()
    venue = models.CharField(max_length=120, null=False)
    
    def __str__(self):
        return self.name + ' - ' + self.venue
    class Meta:
        verbose_name_plural = "Events"
        ordering = ['name']
    
    

class CountryDemographic(models.Model):
    country = models.ForeignKey('Country')
    year = models.ForeignKey('Period')
    population = models.IntegerField(null=False,blank=False)
    
    class Meta:
        unique_together = ("country", "year")
class PriorityAreaStatus(models.Model):
    priority_area = models.ForeignKey('PriorityArea')
    year = models.ForeignKey('Period')
    population = models.PositiveIntegerField()
    number_of_households = models.IntegerField()
    
    class Meta:
        unique_together = ("priority_area", "year")
    
class FacilityAccess(models.Model):
    priority_area = models.ForeignKey('PriorityArea', blank=False)
    technology = models.ForeignKey('Technology', blank=False)
    year = models.ForeignKey('Period', blank=False)
    planned = models.PositiveIntegerField(blank=True, null=True) 
    planned_pop_affected = models.PositiveIntegerField(blank=True, null=True) 
    actual = models.PositiveIntegerField(blank=True, null=True) 
    actual_pop_affected = models.PositiveIntegerField(blank=True, null=True) 
    secured = models.PositiveIntegerField(blank=True, null=True)
    secured_pop_affected = models.PositiveIntegerField(blank=True, null=True) 
    unit_cost = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    house_hold_contribution = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    government_contribution = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    #FacilityAccess._meta.get_field('PriorityArea').rel.to
    #priority_area;
    #priorityarea = PriorityArea.objects.get(pk=priority_area)
    class Meta:
        unique_together = ("priority_area","technology", "year")
    def getpacountru(self):
        return self.priority_area.country
    def getsectorcat(self):
        return self.technology.facility_character.sector_category
        
class SectorPerformance(models.Model):
    country = models.ForeignKey('Country', blank=False)
    sector_category = models.ForeignKey('SectorCategory', blank=False)
    year = models.ForeignKey('Period')
    coverage_target = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    coverage_achieved = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fund_needed = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    fund_mobilised = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True )
    fund_availed = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    fund_used = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    general_comment = models.TextField(blank=True)
    bottlenecks = models.TextField(blank=True)
    measures_taken = models.TextField(blank=True)
    success_challenges = models.TextField(blank=True)
    
    class Meta:
        unique_together = ("country", "sector_category", "year")
    
class PlanningPerformance(models.Model):
    country = models.ForeignKey('Country', blank=False)
    sector_category = models.ForeignKey('SectorCategory', blank=False)
    year = models.ForeignKey('Period')
    plan_preparation_delay = models.PositiveSmallIntegerField(null=True,blank=True)    
    plan_adoption_delay = models.PositiveSmallIntegerField(null=True,blank=True)
    general_comment = models.TextField(blank=True)
    bottlenecks = models.TextField(blank=True)
    measures_taken = models.TextField(blank=True)
    success_challenges = models.TextField(blank=True)
    
    class Meta:
        unique_together = ("country", "sector_category", "year")

class TenderProcedurePerformance(models.Model):
    country = models.ForeignKey('Country',blank=False)
    year = models.ForeignKey('Period')
    tender_procedure_property = models.ForeignKey('TenderProcedureProperty', blank=False)
    registered = models.PositiveSmallIntegerField(null=False,blank=False)
    executed = models.PositiveSmallIntegerField(null=False,blank=False)
    general_comment = models.TextField(blank=True)
    bottlenecks = models.TextField(blank=True)
    measures_taken = models.TextField(blank=True)
    success_challenges = models.TextField(blank=True)
    
    class Meta:
        unique_together = ("country", "tender_procedure_property", "year")

class CommunityApproach(models.Model):
    country = models.ForeignKey('Country', blank=False)
    sector_category = models.ForeignKey('SectorCategory', blank=False)
    year = models.ForeignKey('Period',blank=False, null=False)
    approach_type = models.ForeignKey('CommunityApproachType',blank=False)
    approach_name = models.CharField(max_length=120, null=True, blank=True)    
    description = models.TextField(blank=True)
    cost_per_capita = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    lessons_learnt = models.TextField(blank=True)
    
    class Meta:
        unique_together = ("country", "sector_category", "year")
        ordering = ['country']
    
class PartnerContribution(models.Model):
    country = models.ForeignKey('Country',blank=False)
    sector_category = models.ForeignKey('SectorCategory', blank=False)
    partner = models.ForeignKey('Partner', blank=False)
    annual_contribution = models.DecimalField(max_digits=15, decimal_places=4, null=True,blank=True)
    in_kind_contribution = models.DecimalField(max_digits=5, decimal_places=2, null=True,blank=True)
    financial_contribution = models.DecimalField(max_digits=5, decimal_places=2, null=True,blank=True)
    
    class Meta:
        unique_together = ("country", "sector_category", "partner")
        ordering = ['country']
    
class PartnerEventContribution(models.Model):
    country = models.ForeignKey('Country', blank=False)
    sector_category = models.ForeignKey('SectorCategory', blank=False)
    year = models.ForeignKey('Period')
    partner = models.ForeignKey('Partner', blank=False)
    event = models.ForeignKey('Event', blank=False)
    government_staff_contribution = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    own_staff_contribution = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    
    class Meta:
        unique_together = ("country", "sector_category", "year")
        ordering = ['country']
    
class SWOT(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey('Country', blank=False)
    sector_category = models.ForeignKey('SectorCategory', blank=False)
    overall_challenges = models.TextField(blank=True)
    strengths = models.TextField(blank=True)
    weaknesses = models.TextField(blank=True)
    opportunities = models.TextField(blank=True)
    risks = models.TextField(blank=True)
    mitigation_measures = models.TextField(blank=True)
    kap_recommendations = models.TextField(blank=True)
    conclusion = models.TextField(blank=True)
    class Meta:
        verbose_name_plural = "SWOT"
        ordering = ['sector_category']