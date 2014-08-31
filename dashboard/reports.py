import models
from django.db.models import Sum


class PriorityAreaPopulationReport():
    
    def generate(self,country):
        if not country.name == "[All Country]":
            priority_areas = models.PriorityArea.objects.filter(country=country)
            population = models.PriorityAreaStatus.objects.filter(priority_area__country=country)
            total_population = models.PriorityAreaStatus.objects.filter(priority_area__country=country).aggregate(Sum('population'))
            total_households = models.PriorityAreaStatus.objects.filter(priority_area__country=country).aggregate(Sum('number_of_households'))
        else:
             priority_areas = models.PriorityArea.objects.all()
             population = models.PriorityAreaStatus.objects.all()
             total_population = models.PriorityAreaStatus.objects.all().aggregate(Sum('population'))
             total_households = models.PriorityAreaStatus.objects.all().aggregate(Sum('number_of_households'))
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
        grand_total_cost = sum(item['totals']['pa_total_cost'] for item in country_technology_gaps)
        grand_total_government_contribution = sum(item['totals']['total_government_contribution'] for item in country_technology_gaps)
        grand_total_population_affected = sum(item['totals']['total_population_affected'] for item in country_technology_gaps)
        return {
            'country':country,
            'technology_gap_list':country_technology_gaps,
            'technology':technology,
            'start_year':start_year + 1,
            'end_year':end_year + 1,
            'rows':len(country_technology_gaps),
            'totals':{
                'grand_total_number':grand_total_number,
                'grand_total_cost':grand_total_cost,
                'grand_total_government_contribution':grand_total_government_contribution,
                'grand_total_population_affected':grand_total_population_affected
            }
        }
    
    def get_technology_gap(self,priority_area,technology,start_year,end_year):
        technology_access = models.FacilityAccess.objects.filter(priority_area=priority_area,technology=technology).filter(year__start_year__gt=start_year).filter(year__end_year__lt=end_year)
        technology_gaps = []
        for ta in technology_access:
            number = ta.planned - ta.actual - ta.secured
            unit_cost = self.get_latest_unit_cost(ta.technology,priority_area) 
            total_cost = number or 0 * unit_cost or 0
            government_contribution = total_cost or 0 * ta.government_contribution / 100
            population_affected = ta.planned_pop_affected - ta.actual_pop_affected - ta.secured_pop_affected
            gap = {
                'priority_area':priority_area,
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
            'rows':len(technology_gaps),
            'totals': {
                'total_number':total_number,
                'pa_total_cost':pa_total_cost,
                'total_government_contribution':total_government_contribution,
                'total_population_affected':total_population_affected,
            },
            
        }
            
    def get_latest_unit_cost(self,technology,priority_area):
        technology_access = models.FacilityAccess.objects.filter(priority_area=priority_area,technology=technology).order_by('-year__end_year','-year__end_year').first()        
        return technology_access.unit_cost
    
class TechnologyGapByCategoryReport():    
    
    def generate(self,country,sector_category,start_year,end_year):
        start_year,end_year = start_year - 1,end_year + 1
        priority_areas = models.PriorityArea.objects.filter(country=country)
        gaps_by_category = []
        for p in priority_areas:
            gap = self.get_technology_gaps(p,sector_category,start_year,end_year)
            if gap is not None:
                gaps_by_category.append(gap)
                
        return {
            'country':country,
            'category':sector_category,
            'start_year':start_year + 1,
            'end_year':end_year + 1,
            'gaps_by_category':gaps_by_category,
            'total': {
                'number':sum(item['total']['number'] for item in gaps_by_category),
                'total_cost':sum(item['total']['total_cost'] for item in gaps_by_category),
                'government_contribution':sum(item['total']['government_contribution'] for item in gaps_by_category),
                'population_affected':sum(item['total']['population_affected'] for item in gaps_by_category)                
            },
            'rows':sum(item['rows'] for item in gaps_by_category),
        }
    
    def get_technology_gaps(self,priority_area,category,start_year,end_year):
        facility_characters = models.FacilityCharacter.objects.filter(sector_category=category)
        gaps_by_character = []
        for c in facility_characters:
            gap = self.get_technology_gaps_by_characteristic(priority_area,c,start_year,end_year)
            if gap is not None:
                gaps_by_character.append(gap)
                
        if len(gaps_by_character) < 1:
            return None;
        
        return {
            'priority_area':priority_area,
            'gaps_by_characteristic':gaps_by_character,
            'total': {
                'number':sum(item['total']['number'] for item in gaps_by_character),
                'total_cost':sum(item['total']['total_cost'] for item in gaps_by_character),
                'government_contribution':sum(item['total']['government_contribution'] for item in gaps_by_character),
                'population_affected':sum(item['total']['population_affected'] for item in gaps_by_character)                
            },
            'rows':sum(item['rows'] for item in gaps_by_character),
        }
    
    def get_technology_gaps_by_characteristic(self,priority_area,characteristic,start_year,end_year):
        technologies = models.Technology.objects.filter(facility_character=characteristic)
        gaps_by_technology = []
        for t in technologies:
            gap = self.get_technology_gaps_by_technology(priority_area,t,start_year,end_year)
            if gap is not None:
                gaps_by_technology.append(gap)
        
        if len(gaps_by_technology) < 1:
            return None
        
        return {
            'characteristic':characteristic,
            'gaps_by_technology':gaps_by_technology,
            'total': {
                'number':sum(item['number'] for item in gaps_by_technology),
                'total_cost':sum(item['total_cost'] for item in gaps_by_technology),
                'government_contribution':sum(item['government_contribution'] for item in gaps_by_technology),
                'population_affected':sum(item['population_affected'] for item in gaps_by_technology)                
            },
            'rows':len(gaps_by_technology)
        }
    
    def get_technology_gaps_by_technology(self,priority_area,technology,start_year,end_year):
        technology_access = models.FacilityAccess.objects.filter(priority_area=priority_area,technology=technology).filter(year__start_year__gt=start_year).filter(year__end_year__lt=end_year)
        if not technology_access:
            return None
        # aggregate number
        #planned = technology_access.aggregate(Sum('planned'))['planned__sum']
        planned = technology_access.aggregate(Sum('planned'))['planned__sum']
        actual = technology_access.aggregate(Sum('actual'))['actual__sum']
        secured = technology_access.aggregate(Sum('secured'))['secured__sum']
        
        number = planned - actual - secured
        # aggregate affected population
        pop_planned = technology_access.aggregate(Sum('planned_pop_affected'))['planned_pop_affected__sum']
        pop_actual = technology_access.aggregate(Sum('actual_pop_affected'))['actual_pop_affected__sum']
        pop_secured = technology_access.aggregate(Sum('secured_pop_affected'))['secured_pop_affected__sum']
        population_affected = pop_planned - pop_actual - pop_secured
        # unit cost
        latest_unit_cost = self.get_latest_unit_cost(technology,priority_area) or 0
        latest_gov_contribution = self.get_latest_government_contribution(technology,priority_area) or 0
        return {
            'technology':technology,
            'number':number or 0,
            'unit_cost':latest_unit_cost or 0,
            'total_cost':(number * latest_unit_cost),
            'government_contribution': (number * latest_unit_cost * latest_gov_contribution / 100) ,
            'population_affected':population_affected
        }
        
    def get_latest_unit_cost(self,technology,priority_area):
        technology_access = models.FacilityAccess.objects.filter(priority_area=priority_area,technology=technology).order_by('-year__end_year','-year__start_year').first()        
        return technology_access.unit_cost
    
    def get_latest_government_contribution(self,technology,priority_area):
        technology_access = models.FacilityAccess.objects.filter(priority_area=priority_area,technology=technology).order_by('-year__end_year','-year__start_year').first()        
        return technology_access.government_contribution
    
class EstimatedGapReport():
    
    def generate(self,country,start_year,end_year):
        start_year,end_year = start_year - 1,end_year + 1
        priority_areas = models.PriorityArea.objects.filter(country=country)
        estimated_gaps = []
        
        for p in priority_areas:
            gap = self.get_technology_gap(p,start_year,end_year)
            estimated_gaps.append(gap)
        
        return {
            'country':country,
            'start_year':start_year + 1,
            'end_year':end_year - 1,
            'estimated_gaps':estimated_gaps,
            'rows':len(estimated_gaps),
            'total':{
                'water_supply_total_cost':sum(item['water_supply']['total_cost'] for item in estimated_gaps),
                'sanitation_total_cost':sum(item['sanitation']['total_cost'] for item in estimated_gaps),
                'water_supply_population_affected':sum(item['water_supply']['population_affected'] for item in estimated_gaps),
                'sanitation_population_affected':sum(item['sanitation']['population_affected'] for item in estimated_gaps),
            }
        }
    
    def get_technology_gap(self,priority_area,start_year,end_year):
        water_supply_technologies = models.Technology.objects.filter(facility_character__sector_category__name__startswith='Water')
        sanitation_technologies = models.Technology.objects.filter(facility_character__sector_category__name__startswith='Sanitation')
        
        gap_report_factory = TechnologyGapReport()
        water_supply_gaps,sanitation_gaps = [],[]
        for t in water_supply_technologies:
            gaps_by_year = gap_report_factory.get_technology_gap(priority_area,t,start_year,end_year)
            if gaps_by_year:
                water_supply_gaps.extend(gaps_by_year['pa_technology_gaps'])
        
        for t in sanitation_technologies:
            gaps_by_year = gap_report_factory.get_technology_gap(priority_area,t,start_year,end_year)
            if gaps_by_year:
                sanitation_gaps.extend(gaps_by_year['pa_technology_gaps'])
        water_supply = {
            'total_cost': sum(item['total_cost'] for item in water_supply_gaps),
            'population_affected':sum(item['population_affected'] for item in water_supply_gaps)
        }
        
        sanitation = {
            'total_cost':sum(item['total_cost'] for item in sanitation_gaps),
            'population_affected':sum(item['population_affected'] for item in sanitation_gaps)
        }
        return {
            'priority_area':priority_area,
            'water_supply':water_supply,
            'sanitation':sanitation
        }
        