from django import forms
from dashboard import models


class TechnologyGapByPriorityArea(forms.Form):
    technology = forms.ModelChoiceField(required=True,queryset=models.Technology.objects.all(), widget=forms.Select())
    start_year = forms.IntegerField(required=True)
    end_year = forms.IntegerField(required=True)
    
class TechnologyGapByCategory(forms.Form):
    sector_category = forms.ModelChoiceField(required=True,queryset=models.SectorCategory.objects.all(), widget=forms.Select())
    start_year = forms.IntegerField(required=True)
    end_year = forms.IntegerField(required=True)