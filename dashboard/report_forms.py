from django import forms
from dashboard import models
from dashboard.forms import DynamicChoiceField

YEAR_RANGE = [(i,i) for i in range(1990,2031)]

class TechnologyGapByPriorityArea(forms.Form):
    sector_category = forms.ModelChoiceField(queryset=models.SectorCategory.objects.all(), widget=forms.Select(attrs={'onchange':'FilterFacilityCharacters();'}))
    facility_character = DynamicChoiceField(widget=forms.Select(attrs={'onchange':'FilterTechnologies();', 'disabled':'true'}), choices=(('-1','Select Facility Character'),))
    technology = DynamicChoiceField(widget=forms.Select(attrs={'disabled':'true'}), choices=(('-1','Select Technology'),))
    start_year = forms.ChoiceField(choices=YEAR_RANGE)
    end_year = forms.ChoiceField(choices=YEAR_RANGE)
    
class TechnologyGapByCategory(forms.Form):
    sector_category = forms.ModelChoiceField(required=True,queryset=models.SectorCategory.objects.all(), widget=forms.Select())
    start_year = forms.ChoiceField(choices=YEAR_RANGE)
    end_year = forms.ChoiceField(choices=YEAR_RANGE)
    
class EstimatedGap(forms.Form):
    start_year = forms.ChoiceField(choices=YEAR_RANGE)
    end_year = forms.ChoiceField(choices=YEAR_RANGE)