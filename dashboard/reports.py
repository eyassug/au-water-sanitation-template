from dashboard import models

class PriorityAreaPopultionReport():
    
    def generate(country=None):    
        priority_areas = models.PriorityArea.objects.filter(country=self.country)
        population = models.PriorityAreaStatus.objects.filter(priority_area__country=country)
        
        return {
            'priority_areas':priority_areas,
            'population':population
        }
            
    