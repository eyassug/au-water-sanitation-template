from dashboard import models

class PriorityAreaPopultionReport():
    
    report = ()
    def __init__(self,country):
        self.country = country
        
    def generate():        
        if(self.country):
            priority_areas = models.PriorityArea.objects.filter(country=self.country)
        else:
            priority_areas = models.PriorityArea.objects.all()
        for p in priority_areas:            
            d = models.PriorityAreaStatus.objects.latest()
            r = PriorityAreaPopultion()
            r.population = d.population
            r.name = p.name
            r.households = d.households
            self.report.add(r)
            
            
    class PriorityAreaPopultion():
        name = ""
        population = 0
        households = 0