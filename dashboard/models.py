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
        return self.name + ' - ' + self.facility_character.name + ' - ' + self.facility_character.sector_category.name
    
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
    
class CommunityApproachType(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    is_active = models.BooleanField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Community Approach Types"
    
class Partner(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    mission = models.TextField()
    key_activities = models.TextField()
    is_active = models.BooleanField()
    
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    date = models.DateField()
    venue = models.CharField(max_length=120, null=False, blank=False)
    
    def __str__(self):
        return self.name + ' - ' + self.venue

class CountryDemographic(models.Model):
    country = models.ForeignKey('Country')
    year = models.PositiveSmallIntegerField(null=False,blank=False)
    population = models.IntegerField(null=False,blank=False)
    
class FacilityAccess(models.Model):
    priority_area = models.ForeignKey('PriorityArea')
    technology = models.ForeignKey('Technology')
    year = models.PositiveSmallIntegerField(null=False,blank=False)
    planned = models.DecimalField(max_digits=19, decimal_places=10, null=False)
    actual = models.DecimalField(max_digits=19, decimal_places=10, null=False)
    unit_cost = models.DecimalField(max_digits=19, decimal_places=10, null=False)
    house_hold_contribution = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    government_contribution = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    
class SectorPerformance(models.Model):
    country = models.ForeignKey('Country')
    sector_category = models.ForeignKey('SectorCategory')
    year = models.PositiveSmallIntegerField(null=False,blank=False)
    coverage_target = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    coverage_achieved = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    fund_needed = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    fund_mobilised = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    fund_availed = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    fund_used = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    general_comment = models.TextField()
    bottlenecks = models.TextField()
    measures_taken = models.TextField()
    success_challenges = models.TextField()
    
class PlanningPerformance(models.Model):
    country = models.ForeignKey('Country')
    sector_category = models.ForeignKey('SectorCategory')
    year = models.PositiveSmallIntegerField(null=False,blank=False)
    plan_preparation_delay = models.PositiveSmallIntegerField(null=False,blank=False)    
    plan_adoption_delay = models.PositiveSmallIntegerField(null=False,blank=False)
    general_comment = models.TextField()
    bottlenecks = models.TextField()
    measures_taken = models.TextField()
    success_challenges = models.TextField()

class TenderProcedurePerformance(models.Model):
    country = models.ForeignKey('Country')
    sector_category = models.ForeignKey('SectorCategory')
    year = models.PositiveSmallIntegerField(null=False,blank=False)
    tender_procedure_property = models.ForeignKey('TenderProcedureProperty')
    registered = models.PositiveSmallIntegerField(null=False,blank=False)
    executed = models.PositiveSmallIntegerField(null=False,blank=False)
    general_comment = models.TextField()
    bottlenecks = models.TextField()
    measures_taken = models.TextField()
    success_challenges = models.TextField()

class CommunityApproach(models.Model):
    country = models.ForeignKey('Country')
    sector_category = models.ForeignKey('SectorCategory')
    year = models.PositiveSmallIntegerField(null=False,blank=False)
    approach_type = models.ForeignKey('CommunityApproachType')
    approach_name = models.CharField(max_length=120, null=False, blank=False)    
    description = models.TextField()
    cost_per_capita = models.DecimalField(max_digits=15, decimal_places=4, null=False)
    lessons_learnt = models.TextField()
    
class PartnerContribution(models.Model):
    country = models.ForeignKey('Country')
    sector_category = models.ForeignKey('SectorCategory')
    partner = models.ForeignKey('Partner')
    annual_contribution = models.DecimalField(max_digits=15, decimal_places=4, null=False)
    in_kind_contribution = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    financial_contribution = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    
class PartnerEventContribution(models.Model):
    country = models.ForeignKey('Country')
    sector_category = models.ForeignKey('SectorCategory')
    year = models.PositiveSmallIntegerField(null=False,blank=False)
    partner = models.ForeignKey('Partner')
    event = models.ForeignKey('Event')
    government_staff_contribution = models.DecimalField(max_digits=15, decimal_places=4, null=False)
    own_staff_contribution = models.DecimalField(max_digits=15, decimal_places=4, null=False)
    total_event_contribution = models.DecimalField(max_digits=15, decimal_places=4, null=False)
    
class SWOT(models.Model):
    country = models.ForeignKey('Country')
    sector_category = models.ForeignKey('SectorCategory')
    overall_challenges = models.TextField()
    strengths = models.TextField()
    weaknesses = models.TextField()
    opportunities = models.TextField()
    risks = models.TextField()
    mitigation_measures = models.TextField()
    kap_recommendations = models.TextField()
    conclusion = models.TextField()