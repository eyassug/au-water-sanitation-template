from dashboard import models
from django.db.models import Sum

class PriorityAreaPopulationReport():
    
    def generate(self,country=None):    
        priority_areas = models.PriorityArea.objects.filter(country=country)
        population = models.PriorityAreaStatus.objects.filter(priority_area__country=country)
        total_population = models.PriorityAreaStatus.objects.aggregate(Sum('population'))
        total_households = models.PriorityAreaStatus.objects.aggregate(Sum('number_of_households'))
        
        return {
            'priority_areas':priority_areas,
            'population':population,
            'total_population':total_population['population__sum'],
            'total_households':total_households['number_of_households__sum']
        }
            
    