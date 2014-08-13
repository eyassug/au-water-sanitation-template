from django import forms
from dashboard import models

YEAR_RANGE = [(i,i) for i in range(1990,2031)]

class TechnologyGapByPriorityArea(forms.Form):
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