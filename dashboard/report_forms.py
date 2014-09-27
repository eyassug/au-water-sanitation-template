from django import forms
from dashboard import models
from dashboard.models import Country, PriorityArea, SectorCategory, TenderProcedurePerformance, TenderProcedureProperty

YEAR_RANGE = [(i,i) for i in range(1990,2031)]

class DynamicChoiceField(forms.ChoiceField): 
    def clean(self, value): 
        return value
class PriorityAreaStatus(forms.Form):
    country = forms.ModelChoiceField(required=False,queryset=Country.objects.all(), widget=forms.Select())
class TechnologyGapByPriorityArea(forms.Form):
    sector_category = forms.ModelChoiceField(required=False,queryset=SectorCategory.objects.all(), widget=forms.Select(attrs={'onchange':'FilterFacilityCharacters();'}))
    facility_character = DynamicChoiceField(widget=forms.Select(attrs={'onchange':'FilterTechnologiesNew();'}),)
    technology = forms.ModelChoiceField(required=True,queryset=models.Technology.objects.all(), widget=forms.Select())
    start_year = forms.ChoiceField(choices=YEAR_RANGE)
    end_year = forms.ChoiceField(choices=YEAR_RANGE)
    
class TechnologyGapByCategory(forms.Form):
    sector_category = forms.ModelChoiceField(required=True,queryset=models.SectorCategory.objects.all(), widget=forms.Select())
    start_year = forms.ChoiceField(choices=YEAR_RANGE)
    end_year = forms.ChoiceField(choices=YEAR_RANGE)
    
class EstimatedGap(forms.Form):
    start_year = forms.ChoiceField(choices=YEAR_RANGE)
    end_year = forms.ChoiceField(choices=YEAR_RANGE)