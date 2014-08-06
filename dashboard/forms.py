from django import forms
from dashboard.models import CountryDemographic, FacilityAccess, SectorPerformance, PriorityAreaStatus, Technology
from dashboard.models import Country, PriorityArea, SectorCategory

class CountryStatusForm(forms.ModelForm):
    class Meta:
        model = CountryDemographic
        exclude = ['country']
        
class FacilityAccessForm(forms.ModelForm):
    class Meta:
        model = FacilityAccess
        exclude = ['technology']
    
    def __init__(self, country=None, **kwargs):
        super(FacilityAccessForm, self).__init__(**kwargs)
        if country:
            self.fields['priority_area'].queryset = PriorityArea.objects.filter(country=country)
          
class SectorPerformanceForm(forms.ModelForm):
    class Meta:
        model = SectorPerformance
        exclude = ['country']
        
class PriorityAreaStatusForm(forms.ModelForm):
    class Meta:
        model = PriorityAreaStatus        
        
    def __init__(self, country=None, **kwargs):
        super(PriorityAreaStatusForm, self).__init__(**kwargs)
        if country:
            self.fields['priority_area'].queryset = PriorityArea.objects.filter(country=country)
        
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.PasswordInput()
    
# Cascade Filters
class DynamicChoiceField(forms.ChoiceField): 
    def clean(self, value): 
        return value
    
class DFacilityAccessForm(FacilityAccessForm):    
    sector_category = forms.ModelChoiceField(queryset=SectorCategory.objects.all(), widget=forms.Select(attrs={'onchange':'FilterFacilityCharacters();'}))
    facility_character = DynamicChoiceField(widget=forms.Select(attrs={'onchange':'FilterTechnologies();'}), choices=(('-1','Select Facility Character'),))
    technology = DynamicChoiceField(widget=forms.Select(attrs={'disabled':'true'}), choices=(('-1','Select Technology'),))

class DPriorityAreaStatusForm(PriorityAreaStatusForm):
    country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=forms.Select(attrs={'onchange':'FilterPriorityAreas();'})) 
    priority_area = DynamicChoiceField(widget=forms.Select(attrs={'disabled':'true'}), choices=(('-1','Select Priority Area'),))
    
class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        exclude = ['facility_character']
    
class DTechnologyForm(TechnologyForm):
    sector_category = forms.ModelChoiceField(queryset=SectorCategory.objects.all(), widget=forms.Select(attrs={'onchange':'FilterFacilityCharacters();'}))
    facility_character = DynamicChoiceField(widget=forms.Select(attrs={'onchange':'FilterTechnologies();', 'disabled':'true'}), choices=(('-1','Select Facility Character'),))
    technology = DynamicChoiceField(widget=forms.Select(attrs={'disabled':'true'}), choices=(('-1','Select Technology'),))
    
