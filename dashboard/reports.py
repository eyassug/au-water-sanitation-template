from dashboard import models
from django.db.models import Sum

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
        technology_gap = models.FacilityAccess.objects.filter(priority_area__country=country).filter(year__start_year__gt=start_year).filter(year__end_year__lt=end_year)
        
        return {
            'priority_areas':priority_areas,
            'gaps':technology_gap
        }