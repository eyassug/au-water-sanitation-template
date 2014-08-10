from dashboard import models
from django.db.models import Sum
import random

class PriorityAreaPopulationReport():
    
    def generate(self,country):    
        priority_areas = models.PriorityArea.objects.filter(country=country)
        population = models.PriorityAreaStatus.objects.filter(priority_area__country=country)
        total_population = models.PriorityAreaStatus.objects.aggregate(Sum('population'))
        total_households = models.PriorityAreaStatus.objects.aggregate(Sum('number_of_households'))
        
        return {
            'priority_areas':priority_areas,
            'population':population,
            'total_population':total_population['population__sum'],
            'total_households':total_households['number_of_households__sum'],
            'country':country
        }
            
class TechnologyGapReport():
    
    def generate(self,country,technology,start_year,end_year):
        start_year,end_year = start_year - 1,end_year + 1        
        priority_areas = models.PriorityArea.objects.filter(country=country)
        country_technology_gaps = []
        for p in priority_areas:
            gap = self.get_technology_gap(p,technology,start_year,end_year)
            country_technology_gaps.append(gap)
        
        grand_total_number = sum(item['totals']['total_number'] for item in country_technology_gaps)
        grand_total_cost = sum(item['totals']['total_number'] for item in country_technology_gaps)
        grand_total_government_contribution = sum(item['totals']['total_number'] for item in country_technology_gaps)
        grand_total_population_affected = sum(item['totals']['total_number'] for item in country_technology_gaps)
        return {
            'country':country,
            'technology_gaps':country_technology_gaps,
            'technology':technology,
            'totals':{
                'grand_total_number':grand_total_number,
                'grand_total_cost':grand_total_cost,
                'grand_total_government_contribution':grand_total_government_contribution,
                'grand_total_population_affected':grand_total_population_affected
            }
        }
    
    def get_technology_gap(self,priority_area,technology,start_year,end_year):
        technology_access = models.FacilityAccess.objects.filter(priority_area=priority_area).filter(technology=technology).filter(year__start_year__gt=start_year).filter(year__end_year__lt=end_year)
        technology_gaps = []
        for ta in technology_access:
            number = random.randrange(0, 1000, 2)
            unit_cost = self.get_unit_cost(ta.technology)
            total_cost = number * unit_cost
            government_contribution = total_cost * ta.government_contribution
            population_affected = random.randrange(0, 1000, 2)
            gap = {
                'year':ta.year,
                'number':number,
                'unit_cost': unit_cost,
                'total_cost': total_cost,
                'government_contribution':government_contribution,
                'population_affected': population_affected
            }
            technology_gaps.append(gap)
        
        total_number = sum(item['number'] for item in technology_gaps)
        pa_total_cost = sum(item['total_cost'] for item in technology_gaps)        
        total_government_contribution = sum(item['government_contribution'] for item in technology_gaps)
        total_population_affected = sum(item['population_affected'] for item in technology_gaps)
        return {
            'priority_area':priority_area,
            'pa_technology_gaps':technology_gaps,
            'totals':{
                'total_number':total_number,
                'pa_total_cost':pa_total_cost,
                'total_government_contribution':total_government_contribution,
                'total_population_affected':total_population_affected,
            }
        }
            
    def get_unit_cost(self,technology):
        return random.randrange(1000, 5000, 2)